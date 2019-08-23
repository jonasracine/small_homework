import random

dict = {}
dict['1']=1
dict['2']=2
dict['3']=3


li=[1,3,4]

for key, value in dict.items():
    toAddOrNotToAdd = bool(random.getrandbits(1))
    print(toAddOrNotToAdd)


for key1, value1 in dict.items():
    for key2, value2 in dict.items():
        toAddOrNotToAdd = random.randint(0, 1)
        if toAddOrNotToAdd is 1:
            print("hello")
            print(toAddOrNotToAdd)
