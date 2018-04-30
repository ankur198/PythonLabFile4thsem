a = list()
b = []
c = [1,'a',True]

a.append(1)
# a = [1]
c.count(1)
# 1
c.extend(a)
# c = [1,'a',True,1]
c.sort()
# c = [1,1,'a',True]
c.pop()
# c = [1,1,'a']
c.insert(2,'x')
# c = [1,1,'x','a']
c.clear()
# c = []

