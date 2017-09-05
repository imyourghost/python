#!!! Доделать сортировку по убыванию

# Написать генератор, который возвращает бесконечную последовательность случайных чисел,
# таких что следующее не меньше прошлого
import sys, random
def oogen():
    first = 999
    second = 0
    while first > 0:
        second = random.random()
        yield second
       

if __name__ =='__main__':
    gen = oogen()
    print(gen.__next__(),gen.__next__(),gen.__next__(),
    	gen.__next__(),gen.__next__(),gen.__next__(),gen.__next__(),gen.__next__())
