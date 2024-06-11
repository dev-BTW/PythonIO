#read using readine

with open("Text1.txt",'r',encoding='utf-8') as poem:
    print(poem.readline()) #returns first line
    print(" ")
    print("*"*80)
    print(poem.readlines())  #returns output as list of strings

with open("Text1.txt",'r',encoding='utf-8') as text:
    line = text.readlines()

print(line[-1:]) #Prints last line 
print(line[::-1]) #Prints the list in reverse