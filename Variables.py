#python have no any variable declaratiion method it is specified at the moment we gave the value on it. 
"""
Variables is a container for storing data values
 x= 12 : integers
 name = "Anjal" :string
 weight = 12.22 :float

"""

#now we gonna understanding the variables by taking 3 types of input and print it out

name = input("What's your name ?") #default take input as string
age = int(input("Your age ?")) #integers
weight = float(input("And weight also !")) #float

#Removing white space from user input 
name = name.strip()
age = age.strip()
weight = weight.strip()

# for capitalization : capitalize ()
# for capitalize 1st word of letter : title()
#for splitting user first and last name 
first , last = input("Whats your name ").split(" ")

# printing values 

print("Your details")
print(f"Name : {name} ") #print value using format string
print(f"Split function output of 1st name : {first}")
print(f"Split function output of last name : {last}")
print("Age :" + age) # by concatenation
print("Weight :",weight)

