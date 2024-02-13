#to define function we use def keyword

#Basic function
def basicFunction():
    print("Hello")

#giving parameter to function
def paraFunction(fName):
    print(fName,end=" ")
#default parameter function
def defaultParaFunction(lName='Ghimire'):
    print(lName)
fname=input("Whats your name")
basicFunction()
paraFunction(fname)
defaultParaFunction()
