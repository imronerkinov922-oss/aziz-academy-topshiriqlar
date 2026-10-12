n = int(input())
s = 0
i = 1
while i <= n:
    if i % 2 != 0:
        s += i
    i += 1
print(s)
        