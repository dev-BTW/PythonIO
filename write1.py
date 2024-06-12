"""Basic steps to write data to a file:
1> open file
2> write data
3> close file"""

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

#creats file if does not exist and 'w' specifies write operation is to be performed
#if file has data in it it'll rewrite the data instead of appending 
with open("flowersInfo.txt","w") as plants:
        for plant in data:
              print(plant,file=plants)


newList=[]
#Open the file for reading and append each line to newList list
with open('flowersInfo.txt') as plants:
       for plant in plants:
              newList.append(plant.rstrip())
              
print(newList)