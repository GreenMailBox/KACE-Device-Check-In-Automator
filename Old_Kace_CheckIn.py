#Joshua Hemingway
#7/2/2021

# Import necessary modules
import os
import sys
import csv
import getpass
import datetime

# Set global variables
MIA = []  # List to store hostnames
fields = []  # List to store field names from CSV
user = getpass.getuser()  # Get the current user
runkbot = r'"C:\\Program Files (x86)\\dell\\KACE\\runkbot.exe"'  # Path to the runkbot executable
runamp = r'"C:\\Program Files (x86)\\dell\\KACE\\AMPTools.exe"'  # Path to the AMPTools executable
filename = "C:\\Users\\" + user + "\\Downloads\\devices.csv"  # Path to the CSV file
location = "C:\\Users\\" + user + "\\Downloads\\"  # Location to save files

# Read the CSV file and gather hostnames within the file
def readfile(filename):
    with open(filename, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')  # Delimiter is a comma in the given file
        fields = next(data)  # Removes the first line and stores it into a list called fields
        for row in data:  # Iterate through each row and append the hostname to the MIA list
            MIA.append(row[1])
