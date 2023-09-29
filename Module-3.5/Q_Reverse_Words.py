n = input()
r = n.split()
output = ""

for w in r:
    reverse_w = w[::-1]
    output = output+reverse_w+' '
print(output[:-1])