import sys,os
#SIMPLE TASK MANAGER
def printTasksMenu():
    print("***********************************")
    print("******** SIMPLE TO DO LIST ********")
    print("***********************************")
    print("********* 1. ADD TASK *************")
    print("********* 2. DELETE TASK **********")
    print("********* 3. VIEW TASK ************")
    print("********* 4. MARK COMPLETE ********")
    print("********* 5. EXIT *****************")
    print("--> WHICH OPER TO PERFORM [1,2,3,4,5]")

def addTask():
    print("ADDING A NEW TASK")
    newTask=input("ENTER NEW TASK HERE : ")
    myTasksList.append(newTask)
    print("TASK ADDED")

def deleteTask():
    if len(myTasksList):
        print("DELETING A TASK")
        try:
            delIndex=int(input("ENTER INDEX : "))
            #del myTasksList[delIndex]
            delElem=myTasksList.pop(delIndex)
            print(f"REMOVING TASK FROM THE LIST: {delElem}")
            print("UPDATED LIST IS : ")
            print(" ---->>")
            printTasks()
        except IndexError:
            print("ENTER ONLY INDEX (i.e 1,2 or 3)")
        except ValueError:
            print("ENTER ONLY INDEX (i.e 1,2 or 3)")  
        

    else:        
        print("TASK LIST IS EMPTY") 

def markTaskDone():
    if len(myTasksList):
        print(f"WRITE AND SAVE DATA INTO FILE {fileName}")
        print("---->>>")
        printTasks()
        
        
        while True:
            print("\n****************************")
            print("**** ENTER 1 TO SAVE   ****")
            print("**** ENTER 0 TO EXIT   ****")
            print("****************************")
            isSave=input()
            if isSave in ['1','0']:
                if isSave=='1':
                    with open(fileName,'w') as dataInp:
                        print(f"OPENING FILE {fileName} :")
                        print(f"WRIING DATA INTO FILE {fileName} :")
                        print("WRITING DATA \n   ---->>")
                        for task in myTasksList:
                            dataInp.write(task + '\n')
                        print(f"MARKING TASK DONE AND WRITTEN IN FILE {fileName}")
                        break
                else:
                    print("NOT SAVING DATA!")       
                    break    
                    
            else:
                print("***ENTER VALID OPTIONS!***")
        
    else:
        print("***TASK LIST IS EMPTY!***")    

def printTasks():
    if len(myTasksList):
        print("ALL TASK LIST : ")
        print(" ---->>")
        for i, task in enumerate(myTasksList):
            print(f"{i}. {task}")
    else:
        print("TASK LIST IS EMPTY")    
    
def readFileData():
    with open(fileName,'r') as readData:
        data=readData.readlines()
        myTasksList.clear()
        for newData in data:
            myTasksList.append(newData.strip())

myTasksList=[]    
inputValue='9'
fileName="tasks.txt"

readFileData()

while True:
    #os.system('cls' if os.name == 'nt' else 'clear')
    printTasksMenu()
    inputValue=input()
    os.system('cls' if os.name == 'nt' else 'clear')
    if inputValue in ['1','2','3','4','5']:
        if inputValue == '5':
            print("****EXITING PROGRAM!****")
            sys.exit()
        else:
            if inputValue == '1':
                addTask()
            elif inputValue == '2':
                deleteTask()     
            elif inputValue == '3':
                printTasks()
            else:
                markTaskDone()
    else:
        print("INPUT VALUES ACCORDING TO THE MENU TABLE!")            
            
