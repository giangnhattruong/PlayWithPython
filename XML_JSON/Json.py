
import json

data = '''
[
    {
        "id": "007",
        "name": "James"
    },
    {
        "id": "005",
        "name": "Wayne"
    }
]
'''

info = json.loads(data)
print('Person count:', len(info))

for person in info:
    print('Name:', person['name'])