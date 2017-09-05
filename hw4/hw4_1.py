#!!!!!!нужно доработать!сравнение людей
#Реализовать класс Person, у которого должно быть два публичных поля: age и name. 
#Также у него должен быть следующий набор методов: know(person), который позволяет добавить другого человека в список знакомых. 
#И метод is_known(person), который возвращает знает ли знакомы ли два человека
class Person(object):
    def __init__(self, age, name, friends=None):
        self.age = age
        self.name = name
        self.friends = []

    def know(self, person):
        self.friends.append(person)
        print('{} уже друг {}'.format(self.name, person.name))

    def is_know(self, person):
        if person in self.friends:
            print(' {} друг {}'.format(self.name, person.name))   
        else:
            print('Пацан {} и пацан {} не братухи'.format(self.name, person.name))     

person1=Person(24, 'Vasiya')
person2=Person(29, 'Ilya')
person3=Person(76, 'Egor')

person1.know(person3)
person1.know(person2)

person2.is_know(person3)
person3.is_know(person1)