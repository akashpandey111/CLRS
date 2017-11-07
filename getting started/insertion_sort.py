# Insertion Sort
from operator import ge, gt, lt, add, sub

n = int(input())  # size of input array
a = list(map(int, input().strip().split(' ')))[:n]  # input array
asc = input("Ascending? Y/N")

for i in range(1, n):
    key = a[i]  # card to be inserted
    j = sub(i, 1)
    while ge(j, 0):
        if (asc in ['Y', 'y'] and gt(a[j], key)) or (asc in ['N', 'n'] and lt(a[j], key)):
            # keep shifting previous cards right till the right place for the key is found
            a[add(j, 1)] = a[j]
        j = sub(j, 1)
    a[add(j, 1)] = key  # place card at the right of the card reached after iteration

print(a)
