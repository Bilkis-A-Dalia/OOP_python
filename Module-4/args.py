def all_sum(*numbers):
    sum=0
    print(numbers)
    for num in numbers:
        sum=sum+num
    return sum
total=all_sum(55,33)
print(total)