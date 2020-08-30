import json

path = "book/data/chp3/"
filename = "data-text.json"

json_data = open(path + filename).read()

# load: json to python data
json_list = json.loads(json_data)

print(type(json_list))

for i,item in enumerate(json_list):
    print(i,item)
