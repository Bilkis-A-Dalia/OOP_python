# set : collection of uniqe items
# set={}
numbers=[1,2,3,4,5,6,7,8,9,11,12,14]
print(numbers)
numbers_set=set(numbers)
print(numbers_set)
 
numbers_set.add(55)
print(numbers_set)

numbers_set.remove(7)
print(numbers_set)

for item in numbers_set:
    print(item)

if 99 in numbers_set:
    print('not exists')
elif 9 in numbers_set:
    print('exists')
A = {1,3,5,7}
B = {1,2,3,5,6,7}
print(A & B)
print(A | B) #AuB

