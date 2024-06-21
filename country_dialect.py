#Working with files that contains different separaters
#Since there are many different separaters used we will sniff out the one that is used using sniffer

import csv
filename = "country_info.txt" #here the separator is a '|' character

#with open(filename,'r',encoding='utf-8',newline="") as data:
#    sample = data.read() #reads the entire data so the pointer is at the end of the file
#    data_dialect = csv.Sniffer().sniff(sample)
#    data.seek(0) #.seek() is used to reposition the file pointer to another position, in this case its the begining of the file
#    country_reader = csv.reader(data,dialect=data_dialect)
#    for row in country_reader:
#        print(row)

#more efficient than above code block

with open(filename,'r',encoding='utf-8',newline="") as data:
    sample =""
    for line in range(3):
        sample += data.read() #reads the first three lines only
    data_dialect = csv.Sniffer().sniff(sample)
    data.seek(0) #.seek() is used to reposition the file pointer to another position, in this case its the begining of the file
    country_reader = csv.reader(data,dialect=data_dialect)
    for row in country_reader:
        print(row)