# .csv comma sperated Value
# .txt text file

# with open('message.txt','w') as file:
#     file.write('i am dalia')

# with open('message.txt','a') as file: #append
#     file.write('i am dalia')

with open('message.txt','r') as file: #read
    text = file.read()
    print(text)