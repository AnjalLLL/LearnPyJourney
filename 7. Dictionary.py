def dict():
    students = {"S1":"Anil","s2":"Aman","s3":"Raj"}
    #simple method of printing dictionary
    print(students)
    #display dictionarty content by using loop
    for student in students:
        print(student) #which only prints the key of dictionary
    
    for student in students:
        print(student,students[student], sep=", ")#which print both values and keys)
    
    print("Updating dictionary")
    students.update({"s2":"Keshav"}) #update s2 value Aman to Keshav
    print(students)

def multiValueDist():
    studentDetails = [
        {"name": "Anil","address": "Lalitpur", "age":22},
        {"name":"Aman","address":"Kathmandu","age":23},
        {"name":"Raj","address":"Bhaktapur","age":24}
    ]
    #accssing only name of students
    print("Displaying only name")
    for student in studentDetails:
        print(student["name"])
    
    print("Displaying name , address and age ")
    for student in studentDetails:
        print(student["name"],student["address"],student["age"],sep=", ")

    
def main():
    dict()
    multiValueDist()

main()