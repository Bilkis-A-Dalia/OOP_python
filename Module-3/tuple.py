def multiple():
    return 3,4
print(multiple())

things='pen','tripod','bottle','charger','phone','web cam','sungalss'
print(type(things))
print(things[0])
print(things[-2])
print(things[3:6])

if 'phone' in things:
    print('exists')
for item in things:
    print(item)

items=('book','monitor')
print(items)

# things[0]='wagon'
# print(things) 

print(len(things))

mega=([1,2,3],[4,5,6])
print(type(mega))
print(mega[0])
mega[0][1]=666 #[tuple index][item index]
# tuple cant be change but it can change its item
print(mega)
