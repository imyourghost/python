#Написать функцию, которая принимает на вход список, 
#если в списке все объекты - int. сортирует его. Иначе выбрасывает ValueError
def list_err (*args):
    try:
        for i in args:
            if not isinstance(i,int):
                raise ValueError()

        sort_lis = sorted(args)
        print(*sort_lis)
    except ValueError:
        print('ERR - you have string')
list_err(5,232,7,3)
list_err(5,232,7,3, 'kk')