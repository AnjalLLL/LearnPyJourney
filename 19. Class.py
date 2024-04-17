#now i am going to understand OOP concept in python 
class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

def get_student():
    name = input("Name :")
    house = input("House :")
    student = Student(name,house)

def main():
    get_student()

if __name__ == "__main__":
    main()