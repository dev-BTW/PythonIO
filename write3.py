with open('write3.txt','w') as write3:
    for i in range(10):
        #write3.write(i) #.write will not work as it requires a string type and not anything else
        #print(i,file=write3)
        #.write will work if we explicitly convert int to str
        write3.write(str(i)+"\n")