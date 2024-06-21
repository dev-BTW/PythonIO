#reads OlympicMedals_2020.csv file

import csv
csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename,'r',encoding='utf-8',newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f"column headers {headers}") 
    print("")
    #prints from 2nd line
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
