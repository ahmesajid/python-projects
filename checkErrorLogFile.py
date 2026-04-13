#THIS CODE WILL BE READING ERRORS FROM THE LOGS FILE
from colorama import Fore,Style 

logFileName="file_logs.txt"
keywordToCheckInLogFile=input("Enter keyword to check in log file (i.e error/fail)\n").strip().lower()
error_count=0

try:
    
    with open(logFileName) as fileOpen:
        print("File opened ..")
        print("Reading file data ..")
        eachLineData=fileOpen.readlines()
        #NOW EACH LINE DATA IS IN eachLineData VAR
        print(f"Checking for word {keywordToCheckInLogFile} occurances ..")
        print(f"Checking {keywordToCheckInLogFile} count in file {logFileName}")
        #CHECKING ENTERED WORD IN EACH LINE
        for singleLineData in eachLineData:
            if keywordToCheckInLogFile in singleLineData.lower():
                    print(f" --> "+ Fore.GREEN+"{singleLineData}"+ Style.RESET_ALL)
                    error_count+=1
        #print(eachLineData)
        print("File closed!")
except FileNotFoundError:
    print(f"Can not read file / file not found [{logFileName}]")

if error_count:
     print(f"Word {keywordToCheckInLogFile} found {error_count} times in file {logFileName}")
else:
     print(Fore.RED+ "******No occurance found in file!*****"+ Style.RESET_ALL)     
     #print(Fore.RED + "Error message" + Style.RESET_ALL)