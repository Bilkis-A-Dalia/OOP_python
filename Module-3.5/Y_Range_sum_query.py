n,q = map(int,input().split())
l = list(map(int,input().split()))

for _ in range(q):
    q1,q2 = map(int,input().split())
    s = sum(l[q1-1:q2])
    print(s)


# def calculate_prefix_sum(arr):
#     prefix_sum = [0] * (len(arr) + 1)
#     for i in range(1, len(arr) + 1):
#         prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
#     return prefix_sum

# N, Q = map(int, input().split())
# A = list(map(int, input().split()))

# prefix_sum = calculate_prefix_sum(A)

# for _ in range(Q):
#     L, R = map(int, input().split())
#     sum_lr = prefix_sum[R] - prefix_sum[L - 1]
#     print(sum_lr)
