n = int(input())
i = 1
found = False
while i <= n:
    if i % 4 == 0:
        print(i)
        found = True
        break
    i += 1
if not found:
    print("No")
        