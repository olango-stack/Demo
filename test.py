


import json
import pprint

my_list = ["I", "Love", "Money"]

with open("my.json", "w") as f:
    json.dump(my_list, f)





with open("my.json", "r") as f:
    y = json.load(f)
print(y)



with open("snsevent.json", "r") as f:
    z = json.load(f)
print(z["Records"])