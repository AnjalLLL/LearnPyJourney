def main():
    marks = int(input("Enter your percentage !"))
    checkGrades(marks)

    if checkEligible(marks):
        print("Eligible for further study !!!")
    else:
        print("Not eligible for further study !!!")

def checkGrades(m):
    if m>=90 and m<100:
        print("Obtained Grade 'A+' and", end=" ")
    
    elif m>=80 and m<90:
        print("Obtained Grade 'A' and", end=" ")
    
    elif m>=70 and m<80:
        print("Obtained Grade 'B+' and", end=" ")
    
    elif m>=60 and m<70:
        print("Obtained Grade 'B' and", end=" ")
    
    elif m>=50 and m<60:
        print("Obtained Grade 'C+' and", end=" ")
    
    elif m>=40 and m<50:
        print("Obtained Grade 'C' and", end=" ")
    
    elif m>=30 and m<40:
        print("Obtained Grade 'D+' and",end=" ")
    
    elif m>=20 and m<30:
        print("Obtained Grade 'E' and", end=" ")
    
    else:
        print("Obtained none grade and", end=" ")

def checkEligible(m):
    if m > 50:
        return True
    else:
        return False
    
main()