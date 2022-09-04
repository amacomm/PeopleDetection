import requests
import base64
import json

imp=""
name="people.jpeg"
with open(name, "rb") as image_file:
    imp = base64.b64encode(image_file.read())
param = {
    "image": imp,
    "name": name
    }
resp = requests.post("http://127.0.0.1:8000/recognize", data=param)
j=json.loads(resp.text)
image=base64.b64decode(j["image"])
with open("res.jpeg", 'wb') as f:
    f.write(image)
print(j['count'])
