import argparse
import os
import pandas as pd
import pingouin as pg


def main():
    args = parse_args()
    input_file_name = os.path.basename(args.excel_file)

    try:
        df = pd.read_excel(args.excel_file, sheet_name=0)
    except FileNotFoundError:
        print(f"Error: File '{input_file_name}' not found.")
        return
    except pd.errors.ParserError:
        print(f"Error: Unable to parse '{input_file_name}'. Please make sure it's a valid Excel file.")
        return

    print(f"Calculating Cronbach's Alpha and Confidence Interval for {input_file_name}...")

    try:
        cronbach_alpha, ci = pg.cronbach_alpha(data=df)
    except ValueError:
        print("Error: Unable to calculate Cronbach's Alpha. Make sure the data is formatted correctly.")
        return

    print_results(cronbach_alpha, ci)


def parse_args():
    parser = argparse.ArgumentParser(description="Calculate Cronbach's Alpha and Confidence Interval (CI)")
    parser.add_argument('excel_file', help="Path to the Excel file containing data for calculation")
    args = parser.parse_args()
    return args


def print_results(cronbach_alpha, ci):
    print("\nDone! Here are the results:")
    print(f"Cronbach's Alpha: {cronbach_alpha}")
    print(f"CI: {ci}")


if __name__ == '__main__':
    main()
