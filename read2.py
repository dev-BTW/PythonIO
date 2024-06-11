#better way to open and read a file
#Note how we do not need to close the file 

with open('Text2.txt','r',encoding='utf-8') as file:
    for line in file:
        #print(line,end='')
        #Alternative of end''
        print(line.strip()) #strip removes leading and trailing whitespace characters
        #rstrip removes trailing/space from right side of text and Lstrip accordingly 
