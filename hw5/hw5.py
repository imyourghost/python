from random import choice

# понять, что делать в блоке B!!!
# переделать часть 2. используя "магические методы", попробовать убарть блок __init__


#a) создают список из строк всех нечетных чисел от 1 до 100
list1 = [str(i) for i in range(1,100) if i %2 !=0]

#b) создают список из объектов другого списка кроме итерирумых///////////////не понял 
list2 = ['a', 'b', 'c', [1,2,3], 'addasdasd']
for i in list2:
    print(i)

#c) создают cписок из фразы 'The quick brown fox jumps over the lazy dog'. 
#где каждый объект списка - кортеж из: слова в верхнем регистре, слова в случайном регистре (qUIck) и длины слова

list3 = 'The quick brown fox jumps over the lazy dog'
#list3_1 = [l.upper() +  ' ' + choice([l.lower(), l.upper()]) for l in list3.split()]
#print (list3_1)

#Спизжено
list3_1 = [(word.upper(), ''.join([choice([i.upper(), i.lower()]) for i in word]), len(word)) for word in list3.split()]
print (list3_1)


#2. Написать класс IntToStr, у которого есть одно поле: vlaue. А тип поля - число. 
#Его задачей должно быть реализация возможности сложения чисел и строк. Примеры:
#obj = IntToStr(9.2)
#print(obj + 3) #12.2
#print('a' + obj) #a9.2
#print(obj + 'z') #9.2z

class IntToStr(object):
    def __init__ (self, value):
        self.value = value


    def summ (self, value):
        n = 'f'
        if n == str(n):
            value=str(self.value) + n
            print(value)
            value2= n + str(self.value)
            print(value2)
        else:
            self.value=self.value + n
            print(self.value)

value = IntToStr(9.2)
value.summ(value)

#3. Написать класс Stack, у которого есть два метода push(value) и pop(). 
#Если мы пытаемся сделать pop из пустого стека, нужно выбрасывать исключение IndexError
class Stack(object):
    def __init__(self):
        self.value = None
        self.stack = []

    def push (self, value):
        self.stack.append(value)
        print('Stack ', self.stack, 'added', value)

    def pop (self):
        try:
            if self.stack == []:
                print('stack is empty')
        except IndexError as e:
            print('ERR stack is emty')

st = Stack()
st.pop()
st.push(3)

