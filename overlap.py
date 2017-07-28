a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

dups = []

for numb in a:
    if numb in b:
        dups.append(numb)

#for i in dups:
#    if i == i:
#        dups.remove(i)

print sorted(dups)
