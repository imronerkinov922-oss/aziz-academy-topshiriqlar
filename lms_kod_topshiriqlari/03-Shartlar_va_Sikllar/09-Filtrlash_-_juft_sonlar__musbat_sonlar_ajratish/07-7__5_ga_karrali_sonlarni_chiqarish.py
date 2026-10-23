n = int(input())
parts = input().split()
for p in parts:
    x = int(p)
    if x % 5 == 0:
        print(x)