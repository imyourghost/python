#нужно динамически добавлять ***hw4_2
#Есть класс, который выводи информацию в консоль: Printer, у него есть метод: log(*values). 
#Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *
class Printer:
    def __init__(self, *values):
        self.values=values
        form_text=[]
      
    def logs(self, *values):
        print(self.values)

class FormattedPrinter (Printer):
    def stars (self, *values):
        form_text = len(self.values)
#        print(form_text)
        print('*************************************************')
        print('****', self.values, '****')
        print('*************************************************')


text1 = FormattedPrinter('ttteeexxxttt11','tttteeexxxttt222')
text1.logs(text1)
text1.stars(text1)