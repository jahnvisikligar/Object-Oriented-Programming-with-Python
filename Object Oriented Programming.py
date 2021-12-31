class Triangle:
    
    count = 0
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        Triangle.count +=1
        
    def print_info(self):
        print('Side 1: {}, Side 2: {}, Side 3: {}' .format(self.a,self.b,self.c))
        
    def triangle_count(self):
        print('No. of triangle: {}' .format(Triangle.count))
        
    def __del__(self):
        print('objects gets deleted!')
        Triangle.count -=1
        
    def Perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
    
    def Scalene(self):
        if (self.a != self.b) and (self.b != self.c) and (self.a != self.c):
            return print('scalene triangle')
        else:
            return False

    def Isosceles(self):
        if (self.a == self.b) or (self.b == self.c) or (self.a == self.c):
            return print('isosceles triangle')
        else:
            return False

    def Equilateral(self):
        if (self.a == self.b) and (self.b == self.c) and (self.c == self.a):
            return print('equilateral triangle')
        else:
            return False
            
t1 = Triangle(3, 5, 8)
t1.print_info()
t1.Scalene()
calc_peri = t1.Perimeter()
print('perimeter of t1 triangle =' ,calc_peri)

t2 = Triangle(10, 10, 10)
t2.print_info()
t2.Equilateral()
calc_peri = t2.Perimeter()
print('perimeter of t2 triangle =' ,calc_peri)

t3 = Triangle(3, 4, 3)
t3.print_info()
t3.Isosceles()
calc_peri = t3.Perimeter()
print('perimeter of t3 triangle =' ,calc_peri)

t4 = Triangle(4,5,5)
t4.print_info()
t4.Isosceles()
calc_peri = t4.Perimeter()
print('perimeter of t4 triangle =' ,calc_peri)

del t3

t2.triangle_count()


#inheritance

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def get_older(self,years):
        self.age += years
        
class Programmer(Person):
    
    def __init__(self,name,age,language) -> object:
        super(Programmer,self).__init__(name,age)
        self.language = language
        
    def print_language(self):
        print('fave language: {}'.format(self.language))

p1= Programmer('jahnvi', 24, 'python')
print(p1.name)
print(p1.age)
print(p1.language)

p1.get_older(5)
print(p1.age)
