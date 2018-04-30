class class1:
    '''documentation'''

    #attributes and methods
    pass

#object initialization
a = class1()
a.__setattr__('name','test')

#test
print(a.__getattribute__('name'))