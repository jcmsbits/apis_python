import requests

URL = "https://randomuser.me/api"
# Sin query
response = requests.get(URL)

if response.status_code == 200:
    print(response.text)


# Mediante la Query podemos definir la cantidad de usuarios que queremos
count = int(input("Ingrese la cantidad: "))
params = {
    "results": count
}

response = requests.get(URL, params=params)

if response.status_code == requests.codes.ok:
    payload = response.json()
    result = payload.get("results")
    print(len(result))

    for user in result:
        name = user.get("name") # GET
        # print(f"{name["title"]} {name["first"]} {name["last"]} ")

        print("{title} {first} {last}".format(**name))