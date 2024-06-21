#Read country_info.txt as csv file

import csv
filename = 'country_info.txt'

with open(filename,'r',encoding='utf-8',newline='') as data:
    sample=""
    for line in range(3):
        sample+= data.readline()

    
    data_dialect = csv.Sniffer().sniff(sample)
    data.seek(0)
    reader = csv.DictReader(data,dialect=data_dialect)
    for row in reader:
        print(row)

