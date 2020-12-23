# Kalıtım (inheritance): class'ların birbirinden miras almasıyla olan bir durum
'''
Tanımlanan bir class'ın özelliklerini bir başka class'ın da aynı özellikleri kullanmayı sağlamaktır.
    Person => name, year, age, eat(), run() gibi obje ve method özellikleri gibi

Student(Person), Teacher(Person) => Studen ve Teacher Class'ları, Person özellikleini miras aldı.
Student ve Teacher kendileri için yeni özellikler tanımlayabilir ve bu özellikler Person'a aktarılmaz

'''

# 1
''' 
class Person():
    def __init__(self):         # init bir methodtur
        print("Person class'ı oluştruldu")

class Student(Person):      # Studen, Personun özelliklerini miras (kalıtım) aldı
    pass

p1 = Person()
s1 = Student()
'''

# 2
'''
class Person():
    def __init__(self):         
        print("Person class'ı oluştruldu.")

class Student(Person):          
    def __init__(self):
        Person.__init__(self)                   # eğer bu ifade yazılmasaydı Student methodu Person methoduna baskın gelirdi ve sadece Studen class'ı oluşturuldu çıkardı.
        print("Student class'ı oluşturuldu.")   # ama Person özelliklerini de kullanmak için Person.__init(self) metoduda Student metoduna eklnemeli


# p1 = Person()
s1 = Student()
'''

# 3
class Person():
    def __init__(self, fname, lname):
        self.firsName = fname
        self.lastName = lname         
        print("Person class'ı oluştruldu.")

class Student(Person):          
    def __init__(self):                        # artık burda fname veya lname gibi özellikler tanımlamaya gerek yok çünkü Persondan kalıtım aldık
        Person.__init__(self, fname, lname)                    
        print("Student class'ı oluşturuldu.")

P1 = Person(fname='Ahmet', lname='Çetin')
S1 = Student(fname='Ocean', lname='Freedom')

print(P1.firsName + ' ' + P1.lastName)
print(S1.firsName + ' ' + S1.lastName)