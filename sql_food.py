################################################################################
#  2810ict - Assignment 2
#
#
# Query the Database
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

#function to create new table in the database
def createPreviousViolationsTable():
    try:
        #create table for the previous violations
        create_violations_table = """ CREATE TABLE IF NOT EXISTS previousviolations (
        name TEXT,
        address TEXT,
        zip NUMERIC,
        city TEXT
        );
        """
        cursor.execute(create_violations_table)

        print("New table creation in database was successful")

    except:
        print("Error: Database table creation was a failure :(")
        closeDB(connection)

#function to query the Database
def findBusinessViolations():
    try:
        #let user know that violation codes are being found
        sys.stdout.write("Finding Businesses with previous violations... ")
        sys.stdout.flush()

        #find every different violation code, its description and
        #how many times it occurs
        query = """
        SELECT facility_name, facility_address, facility_zip, facility_city
        FROM inspections i, violations v
        WHERE i.serial_number=v.serial_number
        GROUP BY facility_name
        ORDER BY facility_name;
        """

        #execute query on the violations and inspections tables
        cursor.execute(query)

        #notify user that the query has been found
        print("Violations have been found")

    except:
        #notify user that the query could not be completed
        print("Could not complete query.")

#insert query into new table
def insertDatatoTable():

    try:
        sys.stdout.write("Writing query data to database... ")
        sys.stdout.flush()

        businessdata = cursor.fetchall()

        for row in businessdata:
            _name = row[0]
            _address = row[1]
            _zip = row[2]
            _city = row[3]

            sql = """
            INSERT INTO previousviolations(
            name,
            address,
            zip,
            city
            )
            VALUES( ?, ?, ?, ?)
            """

            values = (_name, _address, _zip, _city)

            #match values with how to insert data and insert into database
            cursor.execute(sql, values)

        #commit data to database
        connection.commit()
        #let user know data has been commited
        print("Data was inserted successfully for previous violations")

    except:
        print("Could not insert data into table")


#function find how many violations each business has (that has at least 1)
def businessViolationCount():
    try:
        #let user know that the businesses are being found
        sys.stdout.write("Finding Businesses with previous violations... ")
        sys.stdout.flush()

        #find every business with a violation code
        query = """
        SELECT facility_name, COUNT(*)
        FROM inspections i, violations v
        WHERE i.serial_number=v.serial_number
        GROUP BY facility_name
        ORDER BY COUNT(*);
        """

        #execute query on the violations database
        cursor.execute(query)

        data = cursor.fetchall()
        for row in data:
            print(row)
        #notify user that violations have been found
        print("Violations have been found")

    except:
        #notify user that the query could not be completed
        print("Could not complete query.")


#run funtions as program
if __name__ == '__main__':
    createPreviousViolationsTable()

    findBusinessViolations()

    insertDatatoTable()

    businessViolationCount()
