################################################################################
#  2810ict - Assignment 2
#
#
# Numpy in Python
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
import numpy as np
import matplotlib.pyplot as plt

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

#functions violations per postcode between july 2015 and december 2017
def findViolationsByPostcode():
    #let user know that violation codes are being found
    sys.stdout.write("Finding Businesses with previous violations... ")
    sys.stdout.flush()

    #find the average amount of violations by postcode per month (30 months)
    query = """
    SELECT facility_zip, strftime('%Y %m', activity_date) as Month, COUNT(*)
    FROM inspections i, violations v
    WHERE i.serial_number=v.serial_number
    GROUP BY facility_zip
    ORDER BY Month, facility_zip
    """

    #execute query on the violations and inspections tables
    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        print(row)

def highestTotal():
    pass

def greatestVariance():
    pass

def perMonth():
    pass

def MvsB():
    pass

#run funtions as program
if __name__ == '__main__':
    findViolationsByPostcode()
