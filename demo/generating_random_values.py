#https://docs.python.org/3/py-modindex.html
import random

for i in range (3):
    print(random.randint(10 , 30))
members = ["jo",  "ok", "okko", "o", "doke"]
leaders = random.choice(members)
print(leaders)