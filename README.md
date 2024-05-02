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
