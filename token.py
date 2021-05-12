import requests
import json
def get_token():
    url = 'http://localhost:8080/api/v1/authentication/auth/'
    query_args = {"username": "admin","password": "test@Pass1"}
    response = requests.post(url, data=query_args)
    return json.loads(response.text)['token']

def get_user_info():
    url = 'http://localhost:8080/api/v1/users/users/'
    token = get_token()
    header_info = { "Authorization": 'Bearer ' + token }
    response = requests.get(url, headers=header_info)
    print(json.loads(response.text))

get_user_info()

