def printMyName(name="Ahmer"):
    #DEFAULT PARAMETER AHMER IF NO ARG
    print("Hello "+ name)

#Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

#ONE LINER LAMBDA FUNCTIONS
#WITHOUR ARG
printMyCName = lambda : print("AHMER BIN SAJID QURESHI")

#LAMBDA WITH ARG
addNums = lambda num1,num2 : num1+num2
print(addNums(2,4))

result = my_function(5, 10, c = 15, d = 20)
#print(result)


#printMyCName()