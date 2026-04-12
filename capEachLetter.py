#CAPILTALIZE EACH LETTER OF THE STTRING

greetString="good morning amazaon fellows"
#SPLITTING STRING AND CONVERTING IT INTO WORDS ARRAY
splitGreetLetters=greetString.split()
splitCapArray=[]
for splitGreetLetter in splitGreetLetters:
    #CAPITALIZING FIRST LETTER AND CONCAT
    #APPENDING IT INTO SPLIT CAP ARRAY (NOW WORDS ARE IN AN ARRAY)
    splitCapArray.append(splitGreetLetter[0].capitalize() + splitGreetLetter[1:])

#PRINTINNG WORDS IN FORM OF STRINGS
print(" ".join(splitCapArray))