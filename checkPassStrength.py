import sys  
def checkUserInpPassStr(userInpPass):
    isNumeric = isAlpha = isSpecial = isUpper = isLower = isLenShort = False
    numLen = alphaLen = specialLen = upperLen = lowerLen = 0
    count=0
    passLen=len(userInpPass)
    #print("Calculating password lenght entered : " , passLen)

    if passLen>=8 :
        print("Entered password length is" , passLen)
        
        #WRITING MAIN CODE HERE
        while count<passLen:
            #print("loop iteration no : ", count+1)
            if userInpPass[count].isalpha():
                isAlpha=True
                alphaLen=alphaLen+1
            if userInpPass[count].isnumeric():
                isNumeric=True 
                numLen=numLen+1
            if not userInpPass[count].isalnum():
                isSpecial=True
                specialLen=specialLen+1
            if userInpPass[count].isupper():
                isUpper=True
                upperLen=upperLen+1
            if userInpPass[count].islower():
                isLower=True  
                lowerLen=lowerLen+1  
            count=count+1     
        #print("UpperCases : ",upperLen )
        #print("LowerCases : ",lowerLen )
        #print("SpecialCases : ",specialLen )
        #print("Numeric : ",numLen )

    else:
        isLenShort=True
        print("Password must be 8 characters long ..")
        print("Exiting code ..")
        sys.exit()

    if isUpper and isLower and isNumeric and isSpecial:
        if upperLen>=3 and lowerLen>=3 and numLen >=3 and specialLen>=3:
            print("very strong password")
        elif numLen==1 and specialLen==1:
            print("weak password / only one special and one numeric")   
        else:
            print("good password")     

    if not isLower:
        print("No lower character found/weak password")  
    if not isUpper:
        print("No upper character found/weak password")
    if not isSpecial:
        print("No special character found/weak password")  
    if not isNumeric:
        print("No numeric character found/weak password")
   



print("Enter Your Password : ")
userInpPass = input()
userInpPass = "".join(userInpPass.split())
print("Entered password is :" , userInpPass)

checkUserInpPassStr(userInpPass)




#we will modify this code later on 