# list,array,colection are same
# index= start from 0 but from last it start from -1
numbers = [32,59,62,48,23,15,20,84,54,90]
print(numbers[3],numbers[-3])

# list(start: end)
print(numbers[2:6])
print(numbers[1:7])

# list(start: end : step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1])
print(numbers[7:2:-1])
print(numbers[:7])
print(numbers[4:])
print(numbers[:])
print(numbers[::-1]) #reverse