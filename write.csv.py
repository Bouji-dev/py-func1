import csv
headerfile = ["state", "population", "city"]
data = [["Tehran", 14, "Tehran"] , ["Fars", 7, "Shiraz"], ["Markazi",3,"Arak"]]

with open("data05.csv",mode="w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headerfile)
    writer.writerows(data)




