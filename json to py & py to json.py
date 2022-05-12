import json
#x = '{"name":"Abhi", "age":29, "desig":"Engg"}'
#y = json.loads(x)
#print(y["age"])
#print(y)
x = {
    "name" : "Abhi",
    "age" : 29,
    "desig" : "Engg"
}

y = json.dumps(x)
print(y)