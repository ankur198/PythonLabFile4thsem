class student:
    '''documentation'''
        
    totalStd = 0 # class attribute

    #constructor
    def __init__(self,name,marks=0):
        self.name = name #object attributes
        self.__marks = marks #private object attribute
        student.totalStd += 1

    #class methods
    def calculateGrade(self):
        if self.__marks > 80:
            return 'A'
        if self.__marks > 60:
            return 'B'
        if self.__marks > 40:
            return 'C'
        return 'D'

    #static method
    @staticmethod
    def getTotalStudents():
        return student.totalStd

a = student('ankur')
b = student('ankur',88)
a.totalStd=10
print(a.totalStd)                  # 10
print(student.getTotalStudents())  #  2
print(a.calculateGrade())          #  D 
print(b.calculateGrade())          #  A
