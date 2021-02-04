people = {
    'Alice': {
        'phone': '2312',
        'addr': 'foo dreiv 23'
    },
    'Beth': {
        'phone': '1232',
        'addr': 'gdsfv 23'
    },
    'Cecil': {
        'phone': '23842',
        'addr': 'sdfgbbb    dreiv 23'
    }
}
lables = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')

# 查找的是电话号还是地址
request = input('Phone number(p) or address (a)?')
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

person = people.get(name, {})
label = lables.get(key, key)
result = person.get(key, 'not available')
print("%s %s is %s." % (name, label, result))
