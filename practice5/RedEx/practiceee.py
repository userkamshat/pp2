import re
text=input()
text=re.findall(r'#[A-Za-z]+',text)
print(text)







