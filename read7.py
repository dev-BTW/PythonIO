with open('country_info.txt','r',encoding='utf-8') as text:
    for row in text:
        line = row.strip('\n').split('|')
        print(line)