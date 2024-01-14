import requests
import pyfiglet
import os
import random
A = '\x1b[1;91m'
E = '\x1b[1;92m'
print(' SAJAD ')
def kid():
    key = input(' key : ')
    lin = input(' ENTAR LIINK : ')
    usr = 'qwertyuiopasdfghjklzxcvbnm'
    m = 0
    while True:
        rnd = str(''.join(random.choice(usr) for i in range(6)))
        link = lin + '?' + rnd
        data = {
            'quantity': '100',
            'link': link,
            'service': '191',
            'action': 'add',
            'key': key }
        m += 100
        url = 'https://smmmain.com/api/v2'
        
        try:
            orde = requests.post(url, data=data).json()
            order = orde['order']
            print(f'''{E}Order {E}: {E}{order} {E}| {E}Send {E}: {E}{m} ''')
        except BaseException:
            print(A + f'''Message_Error {A}: {A}{orde['error']}''')
kid()
