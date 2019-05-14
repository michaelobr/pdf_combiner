import os
import datetime
import calendar
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger
import webbrowser

def combine(tar_pdfs, combined_file_result_name):
    if set(tar_pdfs).issubset(pdfs_in_pricing_que):
        merger = PdfFileMerger()
        for pdf_file in tar_pdfs:
            merger.append(open(pdf_file, "rb"))
        with open(combined_file_result_name, "wb") as fout:
                merger.write(fout)
        webbrowser.open_new(combined_file_result_name)
        print("attempting tp print: " + combined_file_result_name)

# Neccesary date and time setups
now = datetime.datetime.now()
last_two_digit_of_year = str(now.year)
last_two_digit_of_year = last_two_digit_of_year[2:]
today = str(now.month) + "." + str(now.day) + "." + last_two_digit_of_year # this will return the date format of MM/DD/YY
my_date = datetime.date.today()
day_of_week = calendar.day_name[my_date.weekday()] # this will return the day of the week in an english format
if day_of_week == "Friday":
 sunday_date = str(now.month) + "." + str(now.day + 2) + "." + last_two_digit_of_year

# Dirs
testing_que = r"C:\Users\***\Desktop\Python Stuff\test folder"
os.chdir("../../..")
pricing_que = os.getcwd()
manager_check = r"U:\***\Manager Check" 

# set the CWD
os.chdir(pricing_que)

# Get a list of all current pdf files in CWD
pdfs_in_pricing_que = [file_name for file_name in listdir(pricing_que) if isfile(join(pricing_que, file_name)) if file_name.endswith(".pdf")]

# Combine "***" files
invoke_fv = ["*** Account Fair Value Processing.pdf", "*** Account Fair Value Processing.pdf"]
if day_of_week == "Friday":
    combined_file_result_name = "*** FV Invoked " + today + " through " + sunday_date + " & *** FV Invoked " + today + " through " + sunday_date + ".pdf"
else: 
    combined_file_result_name = "*** FV Invoked " + today + " & *** FV Invoked " + today + ".pdf"
combine(invoke_fv, combined_file_result_name)

# Combine "*** FV" files
invesco_fv = ["*** Holdings Download Template.pdf", "***.pdf", "*** Daily FV CheckTemplate.pdf"]
combined_file_result_name = "*** FV " + today + ".pdf"
combine(invesco_fv, combined_file_result_name)

# Combine "*** FV" files
invesco_fv = ["*** InvestOne.pdf", "*** Daily FV CheckTemplate.pdf"]
combined_file_result_name = "*** FV " + today + ".pdf"
combine(invesco_fv, combined_file_result_name)

# Combine "*** Futures GDP" files
if "*** Futures GDP4.pdf" in pdfs_in_pricing_que: # if there is a BBG grab add it into the futures combination
    futures = ["*** Futures GDP.pdf", "*** Futures GDP2.pdf", "*** Futures GDP3.pdf", "*** Futures GDP4.pdf"]
else: 
    futures = ["*** Futures GDP.pdf", "*** Futures GDP2.pdf", "*** Futures GDP3.pdf"]
combined_file_result_name = "*** Futures GDP " + today + ".pdf"
combine(futures, combined_file_result_name)

#Combine "*** Report" files
*** = [] 
***.append("*** IR Report.pdf")
# Find and append any backups for the IR
for f in pdfs_in_pricing_que:
    if "IR Report Backup" in f:
        ***.append(f)

***.append("*** Suspended Report.pdf")
***.append("*** Val Report.pdf")
***.append("Ultimate VAL Assistant.pdf")
***.append("Val Assist GDP Grab.pdf")
# Find and append any backups for the val report
for f in pdfs_in_pricing_que:
    if "Val Backup" in f:
        ***.append(f)

# Find and append the new trades spectra if there is any
for f in pdfs_in_pricing_que:
    if "New Trades Spectra" in f:
        ***.append(f)
# Find and append the new trades gain snap (clean dirty) if there are any
for f in pdfs_in_pricing_que:
    if "Clean Dirty" in f:
        ***.append(f)
# Find and append the new trades gain snap (equity build) if there are any
for f in pdfs_in_pricing_que:
    if "Equity Build" in f:
        ***.append(f)
        
# Find and append the new trades backups if there are any
for f in pdfs_in_pricing_que:
    if "New Trades Backup" in f:
        ***.append(f)

# Add in previous manual backups 
for f in pdfs_in_pricing_que:
    if "Previous Manual" in f:
        ***.append(f)

# Find and append any client pricing instructions relating to new trades if any
for f in pdfs_in_pricing_que:
    if "Client Backup" in f:
        ***.append(f)
***.append("*** Input Audit.pdf")

#print(***)

combined_file_result_name = "*** Report " + today + ".pdf"
combine(***, combined_file_result_name)

# Combine "*** - Missings - OLE" files
if "*** - Missings - OLE2.pdf" in pdfs_in_pricing_que: # if there were securities OLE'd add it into the missing combination
    missings = ["*** - Missings - OLE.pdf", "*** - Missings - OLE2.pdf"]
else:
    missings = ["*** - Missings - OLE.pdf"]
combined_file_result_name = "*** - Missings - " + today + ".pdf"
combine(missings, combined_file_result_name)

# BUG fixes & improvements
# Improved PDF combine speed by a lot from previous version
# Wrote a combine function for code reusage
# Arrays are now hard coded to ensure that files are combined in the correct order 
# Wrote separate file mover .py file to work around bug that said files were still open and couldn't be moved
# Wrote code that will create daily archive folder (for example 11.30.18) to put all our grabs in after combining is completed (if you already made one it will keep the current one)
# Wrote code to combine Missings Report (works both for if there's 1 sheet or 2)
# Wrote code that will include BBG grab with futures save
# Wrote code to name Invoke file correctly on Fridays (to include weekend dates)
# Wrote code to combine the huge *** Report. This is tough due to a varrying amount of files and filenames every day
# Wrote code to fix *** combining bug
# Created a naming matrix for files to share to coworkers so the name the files in a manner they can be recognized by the program
# add try_except: to not produce any output messages (this wasn't ultimately needed)
