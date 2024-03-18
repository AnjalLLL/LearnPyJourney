import csv
def write():
    name = input("Enter the name of students !")
    home = input("Enter the name of students !")
    with open("students.csv",'a') as file:
        writer = csv.DictWriter(file, fieldnames=["name","home"])
        writer.writerow({"name": name,"home":home})
def read():
    students = []
    try:
        with open("students.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)    
        print("Name of students in list are :")
        for student in sorted(students, key = lambda x: x['name'] ):
            print(f"{student['name']} is live in {student['home']}")
    except FileNotFoundError:
        print("Create a file first\n")
        

def main():
    
    
    while(True):
        print("Choose...............\n1.write operation \n 2.read operation \n 3. exit ...!")
        ch = int(input())
        if ch == 1:
            write()
        elif ch ==2:
            read()
        elif ch == 3 :
            exit()
        else:
            print("Enter valid option")
if __name__ == "__main__":
    main()