good_answer=0
user_input = input ('Какой язык мы учим? ')
if user_input.lower() == 'python':
	print ("Красава!\n")
	good_answer += 1
else:
	print ("Неправда\n")

user_input = input ('Какая фамилия у препода? (ответ пишем на инглише) ')
if user_input.lower() == 'sobolev':
	print ("Он самый\n")
	good_answer += 1
else:
	print ("Дядь, стыдно должно быть!\n")

user_input = input ('True and False = ? ')
if user_input.lower() == 'true':
	print ("Так точно\n")
	good_answer += 1
else:
	print ("НЕТ\n")

user_input = input ('4 + 3 = ')
if user_input.lower() == '7':
	print ("Перельман прям!\n")
	good_answer += 1
else:
	print ("пздц...\n")

user_input = input ('str - строка? (да / нет) ')
if user_input.lower() == 'да':
	print ("str - это три буквы, а не строка\n")
	good_answer += 1
else:
	print ("iMalaca\n")

user_input = input ('Python сделает тебя умнее? (да / нет) ')
if user_input.lower() == 'да':
	print ("Не питай себя надеждами, ты безнадежен...\n")
	good_answer += 1
else:
	print ("Все верно, иди лучше пиваса попей\n")

user_input = input ('Python - это жираф? (да / нет) ')
if user_input.lower() == 'да':
	print ("Сам ты жираф)) это червяк!\n")
	good_answer += 1
else:
	print ("Умница!\n")

user_input = input ('Попытка №2 4 + 3 = ')
if user_input.lower() == '7':
	print ("Ну вот зачем ты так? Нормально ведь общались, а ты умничаешь\n")
	good_answer += 1
else:
	print ("Братух, завязывай\n")	

	user_input = input ('Если в python 2.7 написать print(\'YA OSEL\') что получится? ')
if user_input.lower() == 'YA OSEL':
	print ("Бывает...\n")
	good_answer += 1
else:
	print ("Читай маны\n")	

	user_input = input ('И на последок... 242 = ')
if user_input.lower() == '242':
	print ("Не будь, как стадо, фантазируй\n")
	good_answer += 1
else:
	print ("Ты точно уверен, что 242={} ?" .format (user_input))	

print ('\nТы ответил правильно на {} из 10 вопросов... делай выводы' .format (good_answer))

!!!!!!
Переделать
!!!!!!
right_label = 'Правильный ответ!'
wrong_label = 'Неправильный ответ!'

def ask_question(question, right_answer):
	global right_answers
	user_answer = input(question)

	if right_answer == user_answer:
		right_answers +=1
		print(right_label)
	else:
		print(wrong_label)
questions = {
	'Сколько  чегото?': '23',
	'А зачем труляля?': 'asdasd'
}
for k,v in questions.items():
	ask_question(k,v)