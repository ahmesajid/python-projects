import random,sys

#GUESS THE NUMBER GAME
count=0
isNum=False

#GENERATING SYS NUMBER
#sysGenNum=random.randrange(1,100)
sysGenNum=22 #HARD CODING TO PREVENT GITHUB ACTIONS INPUT ERROR/REMOVE THIS LINE WHEN WHILE RUNNING CODE
#GENERATING NUMBER IN RANGE 1-100
print("If you guess in less then 8 inputs , you are a genius!")
while not isNum:
    #userInpNum=int(input("Enter number you are guessing (Must be an integer) : "))
    userInpNum=22 #HARD CODING TO PREVENT GITHUB ACTIONS INPUT ERROR/REMOVE THIS LINE WHEN WHILE RUNNING CODE
    if userInpNum==sysGenNum:
        print(f"Matched!\bYour entered num is :[{userInpNum}]\nSystem generated num is [{sysGenNum}]")
        isNum=True
        sys.exit
    elif userInpNum>sysGenNum:
        print("Number is lower")
    else:
         print("Number is greater")  
    count+=1              

if count<8:
    print(f"***You are a genius!***\nYou guessed the number in {count} times!!")