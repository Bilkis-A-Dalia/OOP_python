def is_palindrome(array):
    n = len(array)
    for i in range(n // 2):
        if array[i] != array[n - i - 1]:
            return False
    return True


N = int(input())
A = list(map(int, input().split()))

if is_palindrome(A):
    print("YES")
else:
    print("NO")