n = int(input())
s = 0
i = 0
while i < n:
    i += 1
    if i  % 9 == 0:
        continue
    s += i
print(s)
    