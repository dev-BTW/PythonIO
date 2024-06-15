import json
languages =[
    ['ABC',1987],
    ['Algol 68',1968],
    ['APL',1962],
    ['C',1973],
    ['Haskell',1990],
    ['Lisp',1958],
    ['Modula-2',1977],
    ['Perl',1987]
]

#NOTE:It is better to use list instead of tuples when working with json as json format
#does not support tuple  

#below code block writes the languages list in the specified json file in json array format which is
#similar to python list an hence can be used back as a list after reading that file 
 
#with open('jsnEx.json','w',encoding='utf-8') as test:
#    json.dump(languages,test)


#below code block reads from the specified json file 

with open('jsnEx.json','r',encoding='utf-8') as test:
    data = json.load(test)

print(data)
print(data[2])