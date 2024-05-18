# Cronbach's Alpha and CI Calculator

## Prerequisites
* Python 3.8 or above
* Python virtual environment

## Installation
1. Create a virtual environment 
2. Install dependencies: ```pip install -r requirements.txt```

## Calculate Cronbach's Alpha and CI
Excel files containing valid data for calculation should be available
### Calculate the first sheet only
```
# Replace "path/to/your/excel/file.xlsx" with the actual path to your Excel file.

python calculate_cronbach_alpha.py "path/to/your/excel/file.xlsx"
```
### Calculate Cronbach's Alpha and CI for multiple sheets by sheet names
```
# Replace "a", "b", "c" with exiting sheet names in your file.

python calculate_cronbach_alpha.py "path/to/your/excel/file.xlsx" --sheet_names a b c
```
Once succeed, the results will be displayed in your terminal.

## Mann-Whitney U Test
- An Excel file containing data for test should be available
- A column "Group name" should be created and each row is assigned to a group
- Create a folder "output" in the project's directory

### Do M-W U Test by column range and group name
```bash
# usage: mann_whitney_u_test.py [-h] [--A_group_name A_GROUP_NAME] [--B_group_name B_GROUP_NAME] [--sheet_name SHEET_NAME] [--column_indexes COLUMN_INDEXES [COLUMN_INDEXES ...]] [--column_range COLUMN_RANGE] excel_file_path
# for example, the following commend does Mann-Whitney U test on columns from F to AP between group Basic and Open Uni
python mann_whitney_u_test.py "path/to/your/excel/file.xlsx" --column_range "F-AP" --A_group_name Basic --B_group_name "Open Uni"
```
It will perform the test between the groups on each column and export the result to output folder.  
