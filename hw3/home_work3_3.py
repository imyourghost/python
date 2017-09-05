#Записать функцию, которая принимает словарь, 
#преобразует все ключи словаря к строкам и возвращает новый словарь
def go_to_string (my_dict):
    new_dict={}
    for k, v in my_dict.items():
        new_key= str(k)
        new_dict.update({k:v})
    print(new_dict)
values= {0:123,1:321,2:'abcd'}
go_to_string(values)
