import requests

URL = "https://visualstudio.microsoft.com/wp-content/uploads/2018/05/cloud.png" # png

response = requests.get(URL, stream= True)
print(response.status_code)

if response.status_code == 200:
    print("Guardando...")
    with open("images/cloud.png", "wb") as img:
        # iter_content recibe como argumento la cantidad de bytes a iterar
        img.write(response.content)
