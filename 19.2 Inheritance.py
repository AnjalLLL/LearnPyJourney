class Student:
    def __init__(self,name) :
        self.name = name
    
    def display(self):
        print(f"My name is {self.name}")
    
class firstSemester(Student):
    def __init__(self, name, course):
        super().__init__(name)
        self.name= name
        self.course= course
    
    def FisrtSemStudent(self):
        print(f"{self.name} from {self.course}")

class secondSemester(Student):
    def __init__(self, name, course):
        super().__init__(name)
        self.name = name
        self.course = course

def main():
    student = Student("Anjal")
    fristsem = firstSemester("Ashmita","Bsc.csit")
    secondsem = secondSemester("Sita","BCA")
    student.display()
    fristsem.FisrtSemStudent()

if __name__ == "__main__":
    main()

