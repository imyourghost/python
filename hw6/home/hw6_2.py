import time
#Реализовать декоратор, который измеряет скорость выполнения функций. Написать три разные функции, задекорировать их и проверить
def decor_add_timer(func):
    def timer(*args):
        start_time = time.time()
        func()
        finish_time = time.time() - start_time
        print('время выполнения составило: ', "{:.7f}".format(finish_time), 'сек')
        print('-------------------------')
    return timer

@ decor_add_timer
def func1():
    print ('[1,2,3]')

@ decor_add_timer
def func2():
    s = 1
    for n in range(1,100):
        s = s + n 
    f = s * n
    print ('результат вычислений f2 = ', f)

@ decor_add_timer
def func3():
	s = [1,2,3,4,5,'sdsd']
	print(s)

func1()
func2()
func3()
