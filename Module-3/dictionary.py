numbers=[1,2,6,7,8,9,11,21,32,43,54,66]
person1= ['kala cad','kalipur',23,'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key:value,key:value}
person={'name':'dalia','age':22,'job':'student','address':'ctg'}
print(person)
print(person['name'])
print(person.keys())
print(person.values())
person['language'] = 'python'
print(person)

for item in person:
    print(item)

# special dictionary looping
for key,value in person.items():
    print(key,value)

