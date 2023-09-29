n = input()
s = []
cnt = ""
for char in n:
    cnt = cnt+char
    if cnt.count("L") == cnt.count("R"):
        s.append(cnt)
        cnt = ""

print(len(s))
for bal_str in s:
    print(bal_str)