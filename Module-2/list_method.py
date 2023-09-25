list=[84,46,78,43]
list.append(45)
print(list)

list.insert(2,84) #index,value
print(list)

if 77 in list:
    list.remove(77)
if 8 in list:
    list.remove(8)
print(list)
last = list.pop()
print(last,list)

if 45 in list:
    index=list.index(45)
    print(index)

sorted = list.sort()
print(list)
list.reverse()
print(list)