import json

data = {
    "author":"id117",
    "name":"aes",
    "description":"",
    "category":"crypto",
    "value":100,
    "flag":open('flag.txt').read(),
}

with open('task.json', 'w') as f:
    f.write(json.dumps(data))