import requests
from getpass import getpass 


password = getpass("Ingresa la contraseña: ")

URL = "http://httpbin.org/basic-auth/josenago/123456"



session = requests.Session()
session.auth = ('josenago', password) # Una tupla (user, password)
response = session.get(URL)

if response.status_code == 200:
    print(response.json())


if response.status_code == 401:
    print(response)
    print("Auntenticación fallida")