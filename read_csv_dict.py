#read csv as dict

import csv
filename = "my_cereals.csv"

with open(filename,'r',encoding='utf-8',newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        print(row)
        