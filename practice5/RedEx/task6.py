import re
text=input()
text=re.sub(r'[ ,.]',':',text)
print(text)