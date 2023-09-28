# lambda

# def doubled(x):
#     return x*2
# result=doubled(44)
# print(result)

doubled=lambda num:num*2
squared = lambda num: num*num
result = doubled(44)
output = squared(9)
print(result,output)

add = lambda x,y: x+y
sum = add(11,13)
print(sum)

# map for all
numbers = [2,43,12,65,87,34]
doubled_nums = map(doubled,numbers)
print(doubled_nums)
doubled_nums2 = map(lambda x: x*2,numbers)
suared_nums = map(lambda x: x*x,numbers)
print(numbers)
print(list(doubled_nums2))
print(list(suared_nums))


# filter for condition
students = [
    {'name':'dalia','age':22},
    {'name':'dora','age':40},
    {'name':'akter','age':57},
    {'name':'bilkis','age':30},
    {'name':'suku','age':38}
]
juniors = filter(lambda student:student['age']<40,students)
fivers = filter(lambda student:student['age']%5==0,students)
print(list(juniors))
print(list(fivers))


