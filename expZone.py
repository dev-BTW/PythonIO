#Git running well

with open("Text1.txt",'r',encoding='utf-8') as text1:
    line1 = text1.readline()
chars = "'"
print(line1)
print(line1.strip(chars))