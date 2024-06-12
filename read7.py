countries ={}

with open('country_info.txt','r',encoding='utf-8') as text:
    for row in text:
        data = row.strip('\n').split('|')
        country,capital,code,code3,dialing,timeZone,currency=data
        #print(country,capital,code,code3,dialing,timeZone,currency,sep='\n\t')
        country_dict ={
            'name':country,
            'capital':capital,
            'code':code,
            'code3':code3,
            'dialing':dialing,
            'timeZone':timeZone,
            'currency':currency,
        }
        #print(country_dict)
        countries[country.casefold()] = country_dict

#print(countries)

choosenCountry = input("Enter a country name: ").casefold
if choosenCountry in countries:
    countryData = countries[choosenCountry]
    print(countryData)