class Student:
    def __init__(self,name,home):
        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name} from {self.home}"
    
    #@name.getter
    def name(self):
        return self._name
    
    #@name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    #@home.getter
    def home(self):
        return self._home
    
    #@home.setter
    def home(self,home):
        if home not in ["Kathmandu","Lalitpur","Bhaktapur","Biratnagar"]:
            raise ValueError("Invalid Addresss")
        self._home = home
    
def main():
        student = get_student()
        print(student)
    
def get_student():
        name = input("Enter name :")
        home = input("Enter name:")
        return Student(name,home)
if __name__ == "__main__":
    main()



        


        
