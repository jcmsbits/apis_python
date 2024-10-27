import requests

URL = "http://httpbin.org/post"

# Si intentamos hacer un get en una direccion que pide POST
# Devuelve un error
# Error 405 el servidor ha recibido tu solicitud, 
# pero el recurso que estás solicitando no es compatible con el método de la solicitud
response = requests.get(URL)

print(response)

response = requests.post(URL)

print(response)

ok = requests.codes.ok
print(ok == 200)

if response.status_code == ok:
    payload = response.json()
    print(payload)

# Para enviar datos al servidor se data, lo cual lo envia en el cuerpo de la petición
data = {
    "username" : "josenago",
    "password" : "12345"
}
response = requests.post(URL, data= data)

if response.status_code == 200:
    payload = response.json()
    print("Forms: ",payload["form"])
    print("Url: ", payload["url"])
    print(response.text)
