"""import re
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)"""

"""import re
txt="The rain in Spain"
x=re.findall("ai",txt)
print(x)"""

"""import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())"""
"""
import re

txt = "The rain in Spain"
x = re.split("\s", txt) #also (after txt,1)only first occurence
print(x)"""

"""
import re
txt="The rain in Spain"
x=re.sub("\s","9",txt)
print(x) #if after txt,2 then only 2whitespace replace with 9

"""
"""
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
"""
"""
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)"""

"""
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())"""