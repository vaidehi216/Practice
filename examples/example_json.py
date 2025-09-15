# import json

# # JSON string
# json_data = '{"name": "Vaidehi", "age": 21, "city": "Surat"}'

# # Convert to Python dictionary
# person = json.loads(json_data)

# print(person["name"])   
# print(person["age"])  


import re
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start()) 