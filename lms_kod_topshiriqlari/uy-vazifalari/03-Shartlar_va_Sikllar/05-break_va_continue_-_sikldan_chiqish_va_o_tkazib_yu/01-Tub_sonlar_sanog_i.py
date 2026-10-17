count = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x < 2:
        continue
    d = 2
    is_prime = 1
    while d * d <= x:
        if x % d == 0:
            is_prime = 0
            break
        d = d + 1
    if is_prime == 1:
        count = count + 1
print(count)