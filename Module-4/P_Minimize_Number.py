n = int(input())
l = list(map(int,input().split()))
a = 0
while all (i%2 == 0 for i in l):
    l=[i//2 for i in l]
    a = a+1
    
print(a)