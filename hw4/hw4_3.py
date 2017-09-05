#Написать класс Animal и Human, сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые). 
#Другие - нет. За что будет отвечать метод is_dangerous(animal)
class Animal (object):
    danger = False

class Human_eater (Animal):
    danger = True

class Vodka_zhivotniy(Animal):
    danger = True


class Human (object):
    def is_dangerous (self, animal_name):
        if animal_name.danger:
            print('Такой живтоный опасно')
            print('-------------') 
        else:
            print('Бери такой животный домой. плов варить ')
            print('-------------') 
proger = Human()

koto_pes = Animal()
tigra = Human_eater()
ezhik_v_tumane = Vodka_zhivotniy()

print('KotoPes:') 
proger.is_dangerous(koto_pes)

print('Tigra:') 
proger.is_dangerous(tigra)

print('Ezhik_v_tumane:') 
proger.is_dangerous(ezhik_v_tumane)

