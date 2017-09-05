#Написать функцию, которая выбрасывает одно из трех исключений:
#ValueError, TypeError или RuntimeError случайным образом
#В месте вызова функции обрабатывать все три исключения
import random
i = []
errors = (RuntimeError, ValueError, TypeError)

def error_gen():

    error_calls = (0,'1','saasd')
    now_error =random.choice(error_calls)

    try:
        new_val = int(now_error)
        if now_error =='1':
            print(i[now_error])
        else:
            raise RuntimeError ('RuntimeError')
    except TypeError:
        print ('TypeError')
    except ValueError:
        print ('ValueError')
    except RuntimeError:
        print ('RuntimeError')
 

error_gen()

try:
    print('----------------')
    raise TypeError()
except TypeError :
        print('TypeError')
try:
    raise ValueError()
except ValueError :
    print('ValueError')
try:
    raise RuntimeError()
except RuntimeError :
    print('RuntimeError')

