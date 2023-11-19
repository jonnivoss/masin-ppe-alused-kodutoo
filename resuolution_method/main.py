# Example usage:
KB = [["a","b","-c","d"], ["a","c","-d"]]
neg_alpha = ["-e"]

new = []
for a in KB:
    for b in a:
        new.append(b)
print(KB,neg_alpha)

new = list(set(new))
print(new) # print all possible lirterals
old_new = new[:]
removable = []
breakeble = False
for i in new:
    for j in new:
        if i.replace("-","") == j.replace("-","") and i != j:
            temp1 = i
            temp2 = j
            removable.append(temp1)
            removable.append(temp2)
            breakeble=True
            break
    if breakeble:
        break

removable = list(set(removable))
print("removables", removable)
for a in removable:
    new.remove(a)

print(new)
if old_new == new:
    print("perses")