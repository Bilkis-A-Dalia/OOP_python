numbers = [84,65,64,87,45,79,64,7]
odds=[]
for num in numbers:
    if num %2== 1 and num %5 == 0:
        odds.append(num)
print(odds)
odd_nums = [num for num in numbers if num%2 == 1]
print(odd_nums)


age_comb=[]
players = ['bilkis','akter','dalia']
ages = [45,84,21]
for player in players:
    print('player:',player)
    for age in ages:
        # print(player,age)
        age_comb.append([player,age])
print(age_comb)
age_comb2 = [(player,age) for player in players for age in ages]
print(age_comb2)