import re
text=input()
print(re.fullmatch(r'ab*',text)is not None)