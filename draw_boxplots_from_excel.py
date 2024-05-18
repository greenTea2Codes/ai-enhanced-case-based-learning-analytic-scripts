import argparse
import pandas as pd

from calculate_percentiles import print_25_50_75_percentiles
from excel_preprocess_utilities import generate_excel_column_range, excel_column_to_index
from mann_whitney_u_test import get_column_values_by_group
from draw_boxplot import draw_and_save_box_plot

def main():
    print('\nStart create box plots...')
    # It takes an Excel file
    # The user can specify groups, e.g., "Basic", and column name for groups
    # The user can specify column range for plotting, e.g., A-AA
    # The script will loop through the range and
    # For each data column, it will get the data for the groups
    # It will create a list or dataframe and use the dataframe for plotting
    args = parse_args()
    df = pd.read_excel(args.excel_file_path, sheet_name=args.sheet_name)
    column_range = args.column_indexes
    if args.column_range is not None:
        start_column, end_column = args.column_range.split("-")
        # print(start_column)
        # print(end_column)
        column_range = generate_excel_column_range(start_column, end_column)

    for col in column_range:
        # print(col)
        col_index = excel_column_to_index(col)
        col_name = df.columns[col_index]
        col_name = col_name[:20]
        print(f"\nPlot column: {col_name}")
        group_a = get_column_values_by_group(df, args.A_group_name, col_index)
        group_b = get_column_values_by_group(df, args.B_group_name, col_index)
        print(args.A_group_name)
        print(f'Size: {str(len(group_a))}')
        print(f'Has NA: {pd.isna(group_a).any()}')
        print_25_50_75_percentiles(group_a)
        print(args.B_group_name)
        print(f'Size: {str(len(group_b))}')
        print(f'Has NA: {pd.isna(group_b).any()}')
        print_25_50_75_percentiles(group_b)
        # print(group_a)
        # print(group_b)
        # plot_df = pd.DataFrame({
        #     args.A_group_name: group_a,
        #     args.B_group_name: group_b
        # })
        draw_and_save_box_plot(
            [group_a, group_b],
            labels=[args.A_group_name, args.B_group_name],
            title=col_name,
            x_label='Groups',
            y_label='Value',
            save_plot=True)


def parse_args():
    parser = argparse.ArgumentParser(description="This script takes a spreadsheet and draw boxplots")
    parser.add_argument("excel_file_path", help="Path to the Excel file containing data for plotting")
    parser.add_argument("--A_group_name", default="Basic",
                        help="The name of the first group in the sheet")
    parser.add_argument("--B_group_name", default="Open Uni",
                        help="The name of the second group in the sheet")
    parser.add_argument("--sheet_name", default=0, help="Name of the sheet for plotting")
    parser.add_argument("--column_indexes", nargs="+", default=['A'],
                        help="The column indexes containing data for plotting, space separated")
    parser.add_argument("--column_range",
                        help="The column index range containing data for test, e.g. A-AA")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
