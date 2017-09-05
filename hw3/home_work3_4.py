#Написать функцию, которая принимает список чисел и возвращает их произвидение
### Переделать под задачу функционального программирования!
def list_multiply (*args):
    my_var = 1
    for arg in args:
        my_var = my_var * arg
    print(my_var)
list_multiply(1,2,3,4,5,6)