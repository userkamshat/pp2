import re
text=input()
print(re.fullmatch(r'a.*b',text)is not None)