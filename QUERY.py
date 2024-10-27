import requests

# La query se escribe despues del signo de interrogación
# y con & agregamos más query
URL = "http://httpbin.org/get?name=josecarlos&password=123456789&email=pepito@elcojo.com"

response = requests.get(URL)

if response.status_code == 200:
    # print(response.text)
    payload = response.json()
    params = payload['args']
    print(params["name"], params["password"], params["email"])


# Una forma más sencilla de hacer un petición con parámetro con requests

params = {
    "name" : "Jose Carlos",
    "apellido" : "Alguno",
    "email" : "seguro@nohaynada.com"
}
URL2 = "http://httpbin.org/get"

response_2 = requests.get(URL2, params=params)

if response_2.status_code == 200:
    payload = response_2.json()['args']
    print(payload["name"])
    print(payload["apellido"])
    print(payload["email"])
    print("Url: ",response_2.json()["url"])