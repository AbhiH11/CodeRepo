import json
# import ast
from functools import reduce

d1 = {
    "k1": ["v1","v2"],
    "k2": ["v3","v4"]
}
# s = reduce(,d1.values())
# s = set(d1.values())
# print(s)
# print(d1.values())
# for sep in d1:
#     if sep== ",":
#         del sep
#     print(d1.values())
# json1 =(json.dumps(list(d1.values()), indent=3))
# print(json1)
# print(type(json1))
# for items in json1:
#     print(items)
# for key,values in d1.items():
#     value = d1.values()
#     print(values)

toJSON = json.dumps(list(d1.values()), indent=4)
# data = json.loads(toJSON)
# # print(data)
print(toJSON)




# str(d1)
# ast.literal_eval(str(d1))
# v1 = d1.values()
# print(d1)
# print(type(d1))
# str(v1)
# print(type(v1))
# values = d1['k1']
# values1 = d1['k2']
# print("values are:", values,values1)
# json = json.dumps(d1.values())
# print(json)
# print(type(json))
# json = json.dumps()
# for item in json:
#     print(item)
# json = json.dumps(values1)
# for value in json:
#     print(value)

# print(json)
# print(json)


# for values in d1:
#     values1 = d1.values()
#     print(values1)
# print (d1.values())
    # values = d1.values()
    # print(values)
# json = json.dumps(d1)
# for values in json1:
# print(json)
