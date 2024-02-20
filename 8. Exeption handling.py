#printing multiplication table by demostrating exeption handling 
def main():
    x = getX("Enter number you want to display multiplication table")
    
    for i in range(10) :
        print(f"{x}*{i+1}={x*(i+1)}")

def getX(text):
    while True:   
        try:
            return int(input(text))
        except ValueError:
            #print("Given value is not an integer ...!")
            pass

main()