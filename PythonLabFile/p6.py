def sorting(s):
    x = str(s).split(",")
    x.sort()
    s = ''
    for y in x:
        s+=y + ','
    s = s.rstrip(',')
    return s

def freqcount(s):
    x = str(s).split(' ')
    d = dict()
    for y in x:
        if y in d:
            d[y]+=1
        else:
            d[y] = 1
    return d

a = 'yo yo honey singh'
b = 'the,quick,brown,fox'
c = freqcount(a)
for x in sorted(c):
    print(x,':',c[x])

print(sorting(b))

'''
-------------------Output-------------------------
honey : 1
singh : 1
yo : 2
brown,fox,quick,the
---------------------EOF--------------------------
'''