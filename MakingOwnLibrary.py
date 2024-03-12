'''This is a simple library which is created to count the word of given user input which can be used in other programs'''
def main():
    count("hello world")
def count(words):
    words = words.split(" ")
    count = 0
    for _ in words:
        count +=1
    print("Total words :" , count) 

if __name__ == "__main__":
    main()


           