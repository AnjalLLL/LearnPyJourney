#here we gonna extract username from given twitter profile url
import re
url = input("URL : ").strip()                     #?: -> THIS MEANS WE GIVE IT TO PARANTHESIS BUT DO NOT NEED TO CAPTURE IT
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
     print(f"Username : {matches.group(1)}")