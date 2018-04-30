a = input("Enter string: ")
a = a.split(' ')
x = []
for i in a:
    if i in x:
        continue
    x.append(i)
for i in sorted(x):
    print(i,end=' ')


'''
-------------------Output-------------------------
Enter string: the the quick brown fox the
brown fox quick the
---------------------EOF--------------------------
'''

