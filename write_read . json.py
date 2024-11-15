import json

d = {"A":100 , "B":200}

with open("data00.json","w") as f:
    json.dump(d,f)

with open("data00.json", "r") as f:
    json.load(f)

