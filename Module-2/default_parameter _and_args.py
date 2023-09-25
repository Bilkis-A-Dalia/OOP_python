# def sum(a,b):
#     result=a+b
#     return result
# total=sum(55,33,55) #defalut parameter
# print(total)

# def sum(a,b,c=0):
#     result=a+b
#     return result
# total=sum(55,33)
# print(total)

# args
def all_sum(a,b,*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num
    return sum
total=all_sum(55,33)
print(total)

def do_a_lot(*args):
    print(args)