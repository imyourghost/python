# Написать генератор, который принимает на вход дату и на каждый вызов выдает следующий день
import datetime

def date_gen(yyyy, mm, dd):
    tomorrow = datetime.date(yyyy, mm, dd)
    while True:
        tomorrow +=datetime.timedelta(days = 1)
        yield tomorrow
        
now = date_gen(2017, 1, 3)
print (now.__next__(), '-->', now.__next__(), '-->',now.__next__())