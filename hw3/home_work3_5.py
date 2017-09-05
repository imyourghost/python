#Написать три функции:do_work, handle_success, handle_error
#do_work(my_list, success_callback, error_callback) принимает на выход 3 аргумента: 
#список, ф-цию для обработки успеха и ф-цию для обработки ошибки.
#Ее задача проверить, что все знач. в списке идут по-возрастанию.
#Если все верно:вызываем success_callback, иначе:error_callback.
#Ф-ция handle_success пишет в консоль инф. об успешном выполнении.
#Ф-ция handle_error выбрасывает ValueError

my_list=[1, 10, 5, 5, 999]
#my_list=[1, 5, 7, 76, 999]
sort_list=sorted(my_list) 

def handle_success ():
    print('Братиш, все ок!')

def success_callback():
	print('Список по возрастанию')
	
def error_callback():
	print('Список не по возрастанию')

def handle_error ():
    try:
        raise ValueError('Ошибка! на входе чет не то')
    except ValueError as e:
        print(e)

def do_work (my_list, success_callback, error_callback):
    if my_list == sort_list:
    	handle_success()
    	success_callback()
    else:
        error_callback()

do_work(my_list, success_callback, error_callback)

print('Вот твой список, дружок: ',my_list)
print('А должен быть:           ',sorted(my_list))



