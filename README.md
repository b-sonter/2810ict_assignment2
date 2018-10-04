# 2810ict_assignment2
## Problem Statement
As more and more industries are becoming data driven, being able to process a large
volume of raw data and produce a concise and insightful summary is becoming more and
more important. As a data consultant for a government agency, you are tasked with
processing some food inspection and health violation data and producing a report
summarising some of the information.

The raw data is provided in 2 excel spreadsheets: (A) Inspections.xlsx and (B) Violations.xlsx.
You will need to complete the below tasks and present your results in a report.
For each python script, you should handle the case where the script has already been run
and therefore the data already exists. This could mean checking to see if the table already
existed in the database, or a specific workbook/worksheet already exists. In each case, you
should decide what to do (display error ? Create a book/sheet with a different name ?
Delete the existing version and re-run the script ?).

A collection of python scripts that deal with sqlite and excel within python have been completed to meet these requirements.

### Clarification on File Structure
* Script (Folder):
  * data (Folder):
    * inspections.xlsx (file)
    * violations.xlsx (file)
  * db_create.py (script)
  * excel_food.py (script)
  * numpy_food.py (script)
  * sql_food.py (script)

## db_create.py
### Overview
A script that opens the given excel files, 'inspections.xlsx' and 'violations.xlsx'. It creates a database through sqlite with two tables, one for each file. The data is then taken from the excel files and put into the database.

### Instructions
* install python
* install sqlite3 and openpyxl
* download file and place in a folder. Create a folder within this folder called 'data', this is where you will download the excel files to.
* if in IDLE, open file and click run. The program will run itself.
* if in a form of terminal, change directory to the location of the file. When in the correct directory run the program by using "python db_create.py".

## sql_food.py
### Overview
A script that performs queries on the data placed within the database in **db_create.py**. It creates a new table containing all businesses that have had at least one violation. The script also takes a query to find how many violations each of these businesses has actually committed and sorts through them via the amount of violations. This information is printed to the console.

### Instructions
* Follow all previous instructions from **db_create.py**. To run this program make sure this file is in the same folder as the previous and this time run "python sql_food.py".

## excel_food.py
This script creates a new excel workbook called "ViolationTypes.xlsx". It renames the first sheet to be called "Violation Types". The data that is put into this spreadsheet is queried from the data placed within the database from **db_create.py**. The query searches through the violations table to sort data into a violation code, its description and how many times it has occured. This information is saved into the created spreadsheet **ViolationTypes.xslx**.

###instructions
* As previously mention make sure all the files are in the correct place and to run this script you will just need to input "python excel_food.py"   
