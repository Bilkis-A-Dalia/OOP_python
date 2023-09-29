def name_me(first,last,**addition):
    name=f'{first} {last}'
    for key, value in addition.items():
        print(key,value)
    return name
name=name_me(first='bilkis', last='akter',title='ms')
print(name)