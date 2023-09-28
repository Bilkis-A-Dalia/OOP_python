name='bilki\'s akter' #escape
name2="bilkis akter"
# multi line string
name3="""
    bilkis akter
    number one
 """
print(name)

#string is a sequence of character
for char in name2:
    print(char)

print(name2[3])
print(name[1:6])
print(name[-3])
print(name[::-1])

# mutable means changeable
# immutable means unchangeable
if 'akter' in name2:
    print('Exists')

print(name2.upper())
print(name2.lower())
