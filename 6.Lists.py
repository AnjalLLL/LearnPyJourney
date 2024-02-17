#creating a list by using list() constructor
def colorsList():
    listOfColors = list(("Red","Yellow","Green","White"))
    length = len(listOfColors)
    print(f"There are {length}  colors in list" )
    for color in listOfColors:
        print(color)
#print list value by indexing value 
def carsList(cars):
    cars = ["Alto","Kia","Nexon","Furtuiner"]
    print("\nThere are following list of cars :")
    for i in range(len(cars)):
        print(i+1,cars[i])

def changeListItems(cars):
    index = int(input("Enter index of list you want to change !  "))
    item = str(input("Enter new items you want to replace in cars list !  "))
    cars[index-1]= item
    print(cars)

def addNewData(cars):
    item = str(input("Enter new items you want to add in cars list !  "))
    cars.append(item)
    print(cars)

def addInSpecificPlace(cars):
    index = int(input("Enter index of list you want to place new items !"  ))
    item = str(input("Enter new items you want to place in cars list !  "))
    cars.insert(index-1,item)
    print(cars)

def removeItems(cars):
    choice = int(input("Enter 1 if you want to remove items by index value !\nEnter 2 if you want to remove items by its name"))
    if choice == 1:
        index = int(input("Enter index of list you want to remove from cars list: "))
        cars.pop(index-1)
        print(cars)
    elif choice == 2:
        item = input("Enter items you want to remove from cars list: ")
        cars.remove(item)
        print(cars)
    else:
        print("Please give the right option")
        removeItems(cars)

def main():
    carslist = ["Alto","Kia","Nexon","Furtuiner"]
    print("Choose from option : \n 1. For seeing color option in cars \n 2.For viewing cars list ")
    print(" 3.For change in car name in list or replace, \n 4. For add new car \n 5. For add new car item in specific place")
    print(" 6.Remove cars from list\n 7. Enter any for exit")
    while True:
        
        choice = int(input("Enter ypur choice"  ))
        if choice == 1:
            colorsList()
        elif choice == 2:
            carsList(carslist)
        elif choice == 3:
            changeListItems(carslist)
        elif choice == 4:
            addNewData(carslist)
        elif choice == 5:
            addInSpecificPlace(carslist)
        elif choice == 6:
            removeItems(carslist)
        else:
            print("Program is terminating........")
            break

main()