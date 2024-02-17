''''To understand split and join function we gonna take input from user and 
split it then join it with "---" and display both conditions '''
def split(Stext):
    Stext = Stext.split(" ")
    print(Stext)
    join(Stext)

def join(Jtext):
    Jtext = "___".join(Jtext)
    print(Jtext)

def main():
    print("Enter anything !")
    txt = str(input())
    split(txt)

main()