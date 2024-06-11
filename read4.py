#Read each line one by one and 
#Break out of code when found the word
wordToFind = str(input("Word to find: "))
with open("Text1.txt","r",encoding="utf-8") as text:
    while True:
        line = text.readline().rstrip()
        print(line)
        if wordToFind in line.casefold():
            break

print("*"*80)
#returns same output as above 
with open("Text1.txt","r",encoding="utf-8") as text:
    for line in text:
        print(line.rstrip())
        if wordToFind in line.casefold():
            break