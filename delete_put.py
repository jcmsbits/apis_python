import requests

# VERBO and Method
# POST = get
# PUT = put
# DELETE = put
# GET = get

URL = "http://httpbin.org/put"

response = requests.put(URL, 
                        params={"name":"Eduardo"},
                        headers={"version": "2.0"},
                        data = {"id" : 1}
                        )

if response.status_code == 200:
    print("Metodo Put",response.text)

response = requests.put(URL, 
                        params={"name":"Eduardo"},
                        headers={"version": "2.0"},
                        data = {"id" : 1}
                        )
if response.status_code == 200:
    print("Metodo Delete",response.text)