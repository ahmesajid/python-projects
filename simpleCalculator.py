#CREATING SIMPLE CALCULATOR USING LOOP AND FUNCTIONS
import time

#MY FUNCTIONS
def addNum(number1, number2):
   return int(number1)+int(number2) 

def subNum(number1, number2):
   return int(number1)-int(number2) 

def divNum(number1, number2):
   return int(number1)/int(number2) 

def mulNum(number1, number2):
   return int(number1)*int(number2) 
def printMenu():
    print("\n#############  SIMPLE CALCULATOR  #############")
    print(  "#############     OPERATIONS      #############")
    print(  "#############      1. ADD         #############")
    print(  "#############      2. SUBTRACT    #############")
    print(  "#############      3. DIVIDE      #############")
    print(  "#############      4. MULTIPLY    #############")
    print(  "#############      5. EXIT    #############")

def startCalulator():
    continueOperations=True
    while continueOperations==True:
        printMenu()
        #INPUT OPERERATION
        operationInp = input("ENTER WHICH OPERATION [1(ADD), 2(SUBTRACT), 3(DIVIDE), 4(MULTIPLY), 5(EXIT)]\n")

        if operationInp=="5":
            print("****EXITING CODE*****\nTHANK YOU FOR USING CALCULATOR!\n")
            continueOperations=False
            break
        elif operationInp in ["1","2","3","4"]:
            #DEFAULT VALUES
            number1=1 
            number2=1
            #PERFORMING OPERATIONS HERE
            number1 = input("ENTER NUMBER 1\n")
            number2 = input("ENTER NUMBER 2\n")

            if operationInp in ["1","2","3","4" ]:
                if operationInp=="1":
                    print("ADDING\nRESULT: ",addNum(number1,number2))
                if operationInp=="2":
                    print("SUBTRACTING\nRESULT: ",subNum(number1,number2))    
                if operationInp=="3":
                    print("DIVIDING\nRESULT: ",divNum(number1,number2))
                if operationInp=="4":
                    print("MULTIPLYING\nRESULT: ",mulNum(number1,number2))   
        else:
            print("***PLEASE ENTER VALID OPERATION***")  
        time.sleep(4)    

startCalulator()        

