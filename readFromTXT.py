#Read text file from same directory 
#syntax open('filename or path','r'),r specifies read only

poem = open('Text1.txt','r',encoding='utf-8')
for line in poem:
    #print(line.strip(),end='')  #.strip removes any leading or trailing whitespaces from character
    print(line,end='') 
    #print(len(line))

poem.close()

