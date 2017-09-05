#Определение НОК
def sp_s(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)
    
x = int(input('a='))
y = int(input('b='))
print('НОК:',nok(x,y))
