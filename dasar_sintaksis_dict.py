users = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'sincere@april.biz',
    'address': {
        'street': 'Kulas Light',
        'suite': 'Apt. 556',
        'city': 'Gwenborough',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1496'
        }
    }
}
print(users)
print(users['name'])
print(users['address']['street'])
print(users['address']['geo']['lat'])

print(users)
print(type(users))
print('\nUbah dict ke json')
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)