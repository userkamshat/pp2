"""import json
import re
data=json.loads(json_data)
pattern=r"^[a-zA-Z0-9.]+[a-zA-Z0-9.-]+\.(edu|com)$"
for user in data:
    if re.match(pattern,user["email"]):
        print(user["name"],user["email"])

"""

from datetime import datetime
dates=[
    "2023-01-01",
    "2023-01-10",
    "2023-02-15",
    "2023-05-01"
]
dates=[datetime.strptime(d,"%Y-%m-%d")for d in dates]
base=dates[0]
for date in dates[1:]:
    difference=(date-base).days
    print(difference)

import math
def distance(p1,p2):
    return math.sqrt(
        (p2[0]-p1[0]**2)+
        (p2[1]-p1[1]**2)
    )

A=(0,0)
B=(3,4)
C=(6,8)
d1=distance(A,B)
d2=distance(B,C)
print(d1+d2)