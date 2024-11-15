import csv
import pandas as pd

headerfile = ["state", "population", "city"]
data = [["Tehran", 14, "Tehran"] , ["Fars", 7, "Shiraz"], ["Markazi",3,"Arak"]]

# with open("data05.csv",mode="w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(headerfile)
#     writer.writerows(data)


data05 = pd.read_csv("data05.csv")
print(data05)
