import csv

with open("data04.csv",mode="r") as f:
    content = csv.reader(f,delimiter="\t")
    for row in content:
        print(row)


print(content)