user_input = input ('Какой язык мы учим? ')
otvet = user_input.lower() == 'Python'
print (otvet ,'\n')

user_input = input ('Какая фамилия у препода? (ответ пишем на инглише) ')
otvet = user_input.lower() == 'Sobolev'
print (otvet ,'\n')

user_input = input ('True and False = ? ')
otvet = user_input == 'True'
print (otvet ,'\n')

user_input = input ('4 + 3 = ')
otvet = user_input == '7'
print (otvet ,'\n')

user_input = input ('str - строка? (да / нет) ')
otvet = user_input == 'да'
print (otvet ,'\n')

user_input = input ('Python сделает тебя умнее? (да / нет) ')
otvet = user_input == 'да'
print (otvet ,'\n')

user_input = input ('Python - это жираф? (да / нет) ')
otvet = user_input == 'нет'
print (otvet ,'\n')

user_input = input ('Попытка №2 4 + 3 = ')
otvet = user_input == '7'
print (otvet ,'\n')

user_input = input ('Если в python 2.7 написать print(\'YA OSEL\') что получится? ')
otvet = user_input == 'YA OSEL'
print (otvet ,'\n')

user_input = input ('И на последок... 242 = ')
otvet = user_input == '242'
print (otvet ,'\n')

print ('\nСпасибо за ответы!')