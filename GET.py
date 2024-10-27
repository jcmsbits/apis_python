import requests

URL = "http://httpbin.org/get"

response = requests.get(URL) # GET

# Haciendo la petición get
print(response)
print(response.status_code)

print(response.text) # Es de tipo string
print(type(response.text))

# Convirtiendo a diccionario
print(response.json()) # dict
print(type(response.json()))

# Dirección de ip
payload = response.json()
print(payload.get("origin"))

# Obteniendo la URL
print(payload["url"])
