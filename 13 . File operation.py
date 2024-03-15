'''There are different operation in files
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists'''

#now we gonna write names of student and read it also

    
def write():
    name = input("Enter the name of students !")
    with open("students.txt",'+a') as file:
        file.write(f"{name} \n" )
def read():
    names = []
    try:
        with open("students.txt") as file:
            for line in file:
                names.append(line.rstrip()) #added student name in list
        #for printing values from list
        print("Name of students in list are :")
        for name in sorted(names):
            print(f"{name}\n")
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