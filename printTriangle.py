n=3
i=0
#CPP METHOD
while i<n:
    #PRINT SPACES
    spaceCount=0
    while spaceCount<n-i-1:
        print(" ", end="")
        spaceCount+=1

    starCount=0
    while starCount<i+1:
        print("*", end="")
        starCount+=1
    #PRINT STARTS
    i+=1
    print("\n", end="")