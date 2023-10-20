EggModel = {
    "Fragile" : 0,
    "Fall" : 0,
    "Liquid" : 0,
    "Spoiled" : 0,
    "Breaks" : 0,
    "Mess" : 0,
    "Smell" : 0
}
EggClauses = [
    ([('Fragile'),('Fall')],('Breaks')),
    ([('Breaks'),('Liquid')],('Mess')),
    ([('Spoiled'),('Breaks')],('Smell'))
]

i = 0
for egg in EggModel:
    if i > 3:
        break
    EggModel[egg] = int(input(f"{egg}  "))
    i+=1

for key in EggModel:
    print(key,EggModel[key])
print()




for clause in range(len(EggClauses)):
    body, head = EggClauses[clause]
    #print(body, head)
    j=0
    for item in body:
        for key in EggModel:
            if (item == key) & EggModel[key] == 1:
                j+=1
        if j==2:
            print("Egg", head)
            EggModel[head] = 1