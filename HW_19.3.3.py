import requests
import json

status = 'available'
# запрос GET
#'''
res_get = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status': {status}},
                   headers = {'accept': 'application/json'})
print(res_get.status_code)
print(type(res_get.json()))

if 'application/json' in res_get.headers['Content-Type']:
    print(res_get.json())
else:
    print(res_get.text)
#'''
# запрос POST ( create user )
#'''
data = {
  "id": 787,
  "username": "pollianna",
  "firstName": "Po",
  "lastName": "Li",
  "email": "tintester@yandex.ru",
  "password": "po-7894561",
  "phone": "78945643213",
  "userStatus": 0
}
headers = { 'accept': 'application/json', 'Content-Type': 'application/json' }

res_post = requests.post(f'https://petstore.swagger.io/v2/user',
                         data = json.dumps(data),
                         headers = headers)
print(res_post.status_code)
print(type(res_post.json()))
if 'application/json' in res_post.headers['Content-Type']:
    print(res_post.json())
else:
    print(res_post.text)

#'''

# запрос PUT  ( update user )
#'''
username = 'pollianna'
data = {
  "id": 787,
  "username": "Pollianna",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
headers = { 'accept': 'application/json', 'Content-Type': 'application/json' }

res_put = requests.put(f'https://petstore.swagger.io/v2/user/{username}',
                         data = json.dumps(data),
                         headers = headers)
print(res_put.status_code)
print(type(res_put.json()))
if 'application/json' in res_put.headers['Content-Type']:
    print(res_put.json())
else:
    print(res_put.text)
#'''
#'''
# запрос DELETE
username = 'Pollianna'
res_del = requests.delete(f'https://petstore.swagger.io/v2/user/{username}',
                         headers ={'accept': 'application/json'})
print(res_del.status_code)
print(type(res_del.json()))
if 'application/json' in res_del.headers['Content-Type']:
    print(res_del.json())
else:
    print(res_del.text)
    #'''