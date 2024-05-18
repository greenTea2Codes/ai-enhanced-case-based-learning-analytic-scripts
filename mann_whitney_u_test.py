import argparse
import pandas as pd
from excel_preprocess_utilities import excel_column_to_index, generate_excel_column_range
from scipy.stats import mannwhitneyu


def main():
    print('\nStart Mann-Whitney U test...')
    args = parse_args()
    # for arg, value in vars(args).items():
    #     print(f"{arg}: {value}")
    df = pd.read_excel(args.excel_file_path, sheet_name=args.sheet_name)
    column_range = args.column_indexes
    if args.column_range is not None:
        start_column, end_column = args.column_range.split("-")
        # print(start_column)
        # print(end_column)
        column_range = generate_excel_column_range(start_column, end_column)

    # print(df)
    # run Mann-Whitney U test in a loop
    test_results = []
    for col in column_range:
        # print(excel_column_to_index(col))
        col_index = excel_column_to_index(col)
        col_name = df.columns[col_index]
        print(f"\nTest column: {col_name}")
        group_a = get_column_values_by_group(df, args.A_group_name, col_index)
        group_b = get_column_values_by_group(df, args.B_group_name, col_index)
        # print(group_a)
        # print(group_b)
        u_statistic, p_value = mannwhitneyu(group_a, group_b)
        print(f"U Statistic: {u_statistic}")
        print(f"P-Value: {p_value}")

        # Interpretation
        if p_value < 0.05:
            print("There is a significant difference between the two groups")
        else:
            print("There is no significant difference between the two groups")

        # export the result as a spreadsheet
        test_results.append({
            'Column name': col_name,
            'U Statistic': u_statistic,
            'p value': p_value,
            'Significant (p < 0.05)': p_value < 0.05
        })
    results_df = pd.DataFrame(test_results)
    # print(results_df)
    output_file = f'./output/mann_whitney_u_test_results_between_{args.A_group_name}_and_{args.B_group_name}.xlsx'
    results_df.to_excel(output_file, index=False)


def parse_args():
    parser = argparse.ArgumentParser(description="This script takes a spreadsheet and runs Mann-Whitney U test")
    parser.add_argument("excel_file_path", help="Path to the Excel file containing data for test")
    parser.add_argument("--A_group_name", default="Basic",
                        help="The name of the first group in the sheet")
    parser.add_argument("--B_group_name", default="Open Uni",
                        help="The name of the second group in the sheet")
    parser.add_argument("--sheet_name", default=0, help="Name of the sheet for test")
    parser.add_argument("--column_indexes", nargs="+", default=['A'],
                        help="The column indexes containing data for test, space separated")
    parser.add_argument("--column_range",
                        help="The column index range containing data for test, e.g. A-AA")
    args = parser.parse_args()
    return args


# Function to get values from a specific column based on "Group Name"
def get_column_values_by_group(df, group_name, column_index):
    # Filter the DataFrame based on the "Group Name"
    filtered_df = df[df['Group Name'] == group_name]

    # Select the column by index
    selected_column = filtered_df.iloc[:, column_index]

    # Convert the selected column to an array (or list)
    values_array = selected_column.values

    return values_array


if __name__ == '__main__':
    main()


