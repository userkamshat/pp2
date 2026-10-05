import re
text=input()
print(re.fullmatch(r'ab{2,3}',text)is not None)