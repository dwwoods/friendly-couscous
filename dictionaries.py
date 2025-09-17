# key: value # i.e. key value pairs

customer = {
    'name': 'John Smith',
    'age': 22,
    'is_verified': True
}

print(customer)
print(customer.get('name'))
#or#
print(customer['name'])
print(customer.get('city')) #will return None as that's not in the Dictonary
print(customer.get('city', "unknown")) # giving it a default value

customer["name"] = "Jack Smith"
print(customer)
customer["Birthday"] = "1 Jan 1980"
print(customer)