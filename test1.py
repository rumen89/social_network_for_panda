import json

try:
    with open('network.json', 'r') as f:
        dict = json.dumps(json.load(f), indent=4)
except:
    dict = {}

print(dict)

dict['a'] = ['a']
dict['b'] = ['b']

with open('network.json', 'w') as f:
    json.dump(dict, f, indent=4)
