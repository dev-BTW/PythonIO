#More about .strip

with open('Text1.txt','r',encoding='utf-8') as text:
    line = text.readline()

print(line)

chars = "'Twasebv"
print(line.strip(chars))

#.removeprefix .removesuffix
Twas_removed = line.removeprefix("'Twas")
Toves_removed = line.removesuffix('toves') #works from python 3.9 onwards
print(f"{Twas_removed}\n{Toves_removed}")