def convert(text):
    emoji_mapTable= {
       ":)": "🙂",
       ":(": "🙁"
    }
    for key , values in emoji_mapTable.items():
        text = text.replace(key,values)
    print(text)
def main():
    text = input("Enter a sentence !")
    convert(text)

main()