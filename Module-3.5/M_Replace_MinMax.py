n=int(input())
l=list(map(int,input().split()))
min=min(l)
max=max(l)
min_in=l.index(min)
max_in=l.index(max)
l[min_in]=max
l[max_in]=min
print(*l)