#реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.

def write_to_file(data):
    file = open('read.txt', 'w')
    file.write(data)
    file.close()

def read_file_data():
    file = open('read.txt','r')
    print(file.read())
    file.close()

write_to_file('message1')

read_file_data()





