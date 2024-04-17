import re;
name = input("Enter your name\n").strip()
if matches := re.search(r"^([a-zA-Z]+), *([a-zA-Z]+)$",name): #python walrus opeartpr is introducrd 
    name = matches.group(2)+" "+matches.group(1)
print(f"Hello, {name}")