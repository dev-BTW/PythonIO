#.strip() .lstrip() .rstrip()

with open("Text2.txt",'r',encoding='utf-8') as text:
    line = text.readline()

chars ="'"
print(line.strip()) #strips whitespaces from both side
print(line.rstrip()) #from right side i.e end of line
print(line.lstrip()) #from left side i.e from beginning of line

print(line.strip(chars)) 