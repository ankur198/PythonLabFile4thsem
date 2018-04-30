a = 2
b = 3
c = 2

print(id(a))
print(id(b))
print(id(c)) 
#a and c have same id

#type is used to check object's class/type
if type(a) == int: 
    print("a is int type")


'''
-------------------Output-------------------------
1599103232
1599103264
1599103232
a is int type
---------------------EOF--------------------------
'''