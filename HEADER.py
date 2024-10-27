import requests

URL = "http://httpbin.org/post"

# Se deberia usar así
# Query -> GET
# Cuerpo de petición -> POST
# Encabezado -> Para todos

headers = {
    'course' : "Curso de Python",
    "version" : "2.0",
    "author" : "Eduardo Ismael"
}
params = {
    "platform" : "Codigo Facilito"
}
# No son excluyentes

data = {
    "username" : "josenago",
    "password" : "12345"
}
response = requests.post(URL, headers=headers, params=params, data=data)

if response.status_code == 200:
    print(response.text)