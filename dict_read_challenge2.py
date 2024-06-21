import csv
filename = 'country_info.txt'
countries ={}

with open(filename,'r',encoding='utf-8',newline='') as data:
    sample =""
    for line in range(3):
        sample+=data.readline()
    data_dialect = csv.Sniffer().sniff(sample)

    data.seek(0)
    reader = csv.DictReader(data,dialect=data_dialect) #uses headers as keys for dictionaries
    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()]=row

while True:
    choosenCountry = input("Enter a country name or quit to exit: ").casefold()
    if choosenCountry in countries:
        countryData = countries[choosenCountry]
        print(f"capital of {countryData['Country']} is {countryData['Capital']}")

    elif choosenCountry == 'quit':
        break