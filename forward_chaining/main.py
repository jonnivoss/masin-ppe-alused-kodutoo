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

a = [0,0,0,0]
def change_states(a):
    i = 0
    EggModel["Breaks"] = 0
    EggModel["Mess"] = 0
    EggModel["Smell"] = 0
    for egg in EggModel:
        if i < 4:
            EggModel[egg] = int(a[i])
            i+=1
        else:
            break

def print_current():
    i = 0
    for key in EggModel:
        if i < 4:
            print(f" {EggModel[key]} | ",end="")
        else:
            print(f" |  {EggModel[key]} ", end="")
        i +=1
    print("\\")

def check():
    for clause in range(len(EggClauses)):
        body, head = EggClauses[clause]
        #print(body, head)
        j=0
        for item in body:
            for key in EggModel:
                if (item == key) & EggModel[key] == 1:
                    j+=1
            if j==2:
                EggModel[head] = 1

for i in range(16):
    a = [0,0,0,0]
    sg = bin(i)
    reee = sg.replace("0b","")
    sentaur = reee.zfill(4)
    change_states(sentaur)
    check()
    print_current()

