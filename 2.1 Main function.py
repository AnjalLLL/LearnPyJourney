#we can also write main function code in before the other function 

def main():
    print("Enter two numbers to add")
    x=int(input())
    y=int(input())
    print(f"Sum of {x} and {y} is {addNumbers(x,y)}")

def addNumbers(a,b):
    return a+b

main()