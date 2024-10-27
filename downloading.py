import requests

URL = "https://codigofacilito.com/images/cody" # png
URL_2 ="https://developer.mozilla.org/pimg/aHR0cHM6Ly9zdGF0aWM0LmJ1eXNlbGxhZHMubmV0L3V1LzIvMTU0ODUwLzE3MjUwNDUzMjAtMTQ1NngxODBfQS5wbmc%3D.gQddojNaSIEGMqbwfPHt8WRmseAFkInV23TWc4LtSsY%3D"
response = requests.get(URL_2, stream= True)
print(response.status_code)

if response.status_code == 200:
    print("Guardando...")
    with open("images/ai-powered.png", "wb") as img:
        # iter_content recibe como argumento la cantidad de bytes a iterar
        for chunk in response.iter_content(1024):
            img.write(chunk)
