#Substring
#زیررشته
import re

text=input().upper()
if re.search("(AB.*BA)|(BA.*AB)", text):
    print("YES")
else:
    print("NO")
