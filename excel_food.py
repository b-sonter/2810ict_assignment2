################################################################################
#  2810ict - Assignment 2
#
#
# Excel via Python
#
#
# Created by Brianna Sonter | s2930629
#
################################################################################

#imports
import re
import sqlite3
import openpyxl
from openpyxl import *
import sys

#function to connect to Database
def connectDB():
    try:
        db_fname = "data/foodData.db"
        connection = sqlite3.connect(db_fname)
        #let user know that connection to the database was successful
        print("Connected to Database successfully")
        return connection

    except:
        #let user know that connection to database couldnt be created
        print("Error: Could not connect to Database")

#function to close the connection to database
def closeDB(_connection):
    try:
        connection = _connection
        connection.close()
        print("Connection closed")

    except:
        #let user know database was unable to close
        print("Error: Was unable to close connection to Database")

#Open database
connection = connectDB()
cursor = connection.cursor()

#filename and set up for saving
workbook_fn = 'data\ViolationTypes.xlsx'

#create new workbook
wb = openpyxl.Workbook()
sheet = wb.active

#function to create new workbook sheet
def violationTypesSheet():
    try:
        #rename sheet and save changes
        sheet.title = "Violations Types"
        wb.save(workbook_fn)

        #notify user that workbook has been created
        print("Violations Types workbook created.")

    except:
        #notify user that violations workbook could not be created.
        print("Unable to create Violations Types Workbook.")

#function to query the Database
def findViolations():
    try:
        #let user know that violation codes are being found
        sys.stdout.write("Finding Violation Codes... ")
        sys.stdout.flush()

        #find every different violation code, its description and
        #how many times it occurs
        codes = """
        SELECT violation_code, violation_description, COUNT(*)
        FROM violations
        GROUP BY violation_code
        ORDER BY violation_code;
        """

        #execute query on the violations database
        cursor.execute(codes)
        #notify user that violations have been found
        print("Violations have been found")

    except:
        #notify user that the query could not be completed
        print("Could not complete query.")


#function to write data into new sheet
def saveViolationsData():
    try:
        sys.stdout.write("Writing Violations into Violations Types Workbook... ")
        sys.stdout.flush()

        #get all data from query 'codes'
        violationTypeData = cursor.fetchall()

        #add data in rows to the spreadsheet
        for data in violationTypeData:
            sheet.append(data)
            wb.save('data\ViolationTypes.xlsx')
            #display data that was inserted into spreadsheet
            print(data)

        #notify user that data has been input into excel spreadsheet
        print("Violation Data has been inserted.")

    except:
        #notify user that data could not be saved to the spreadsheet
        print("Data could not be inserted.")



#run funtions as program
if __name__ == '__main__':
    violationTypesSheet()

    findViolations()

    saveViolationsData()
