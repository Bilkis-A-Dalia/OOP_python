n = int(input())
l = list(map(int,input().split()))
b = {}
for i in l:
    if i in b:
        b[i] = b[i]+1
    else:
        b[i] = 1

result = 0
for key,value in b.items():
    if value != key:
        if key < value:
            result = result+(value-key)
        else:
            result = result+value
print(result)
