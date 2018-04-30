f = open('TextFile1.txt','r')
c = f.read()
print(c)
f.close()
f = open('TextFile1.txt','w')
f.write(c)
f.flush()
f.close()

'''
-------------------Output-------------------------
hello
how are you?
---------------------EOF--------------------------
'''
