def ingly(s):
    if str(s).endswith("ing"):
        return str(s) + 'ly'
    else:
        return s + 'ing'

def dolloring(s):
    x = s.split(" ")
    for i in range(len(x)):
        c = len(x[i]) - 1
        x[i] = x[i][0] + "$" * c
    s = ""
    for y in x:
        s+=y + " "
    return s

a = "abc"
b = "inkling"
c = "the quick brown fox"
print(ingly(a))
print(ingly(b))
print(dolloring(c))

'''
-------------------Output-------------------------
abcing
inklingly
t$$ q$$$$ b$$$$ f$$
---------------------EOF--------------------------
'''