import os
import datetime
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger
import webbrowser

# Neccesary date and time setups
now = datetime.datetime.now()
last_two_digit_of_year = str(now.year)
last_two_digit_of_year = last_two_digit_of_year[2:]
today = str(now.month) + "." + str(now.day) + "." + last_two_digit_of_year

# Dirs
pricing_que = r"U:\***"
os.chdir("../../..")
pricing_que = os.getcwd()
manager_check = r"U:\***\Manager Check" 

# Set CWD
os.chdir(pricing_que)

# Get a list of all current pdf files in CWD
pdfs_in_pricing_que = [file_name for file_name in listdir(pricing_que) if isfile(join(pricing_que, file_name)) if file_name.endswith(".pdf")]

# Make a new directory for the day if one is not already created 
if os.path.isdir(today) == False:
    os.mkdir(today)

#Archive all pdfs to the today directory
for file_name in pdfs_in_pricing_que:
    os.rename(file_name, pricing_que + "\\" + today + "\\" + file_name)

# All our pdfs are now in the pricing_que\today folder, so let's chdir to there
os.chdir(today)

# Put combined files into the manager check folder
for file_name in pdfs_in_pricing_que:
    if today in file_name:
        os.rename(file_name, manager_check + "\\" + file_name)