###!!!!!!!!!!!! Записать нужно тоже самое, что выводится в print
#получать при помощи requests данные сайта https://jsonplaceholder.typicode.com/, 
#выводить в консоль все пары "ключ-значение", сохранять полученный json в файл.
import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com')
for k, v in response.headers.items():
    print(k, ' :: ', v)
file = open('json.txt','w')
file.write(json.dumps(dict(response.headers)))
file.close()