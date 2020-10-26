import requests
import re

#Declare variables
URL = "https://host/page.php"
PARAM = ""

r = requests.post(URL,data = {PARAM:"'INSERT INTO users WHERE 1"})
resp = r.text
match = re.match(r'SQL', resp)

if match:
    print("Parameter " + PARAM + " appears to be injectable.")
    print(resp)
    print("For further testing of this vulnerability, use SQLMap")
else:
    print("Parameter " + PARAM + " doesn't appear to be vulnerable")




