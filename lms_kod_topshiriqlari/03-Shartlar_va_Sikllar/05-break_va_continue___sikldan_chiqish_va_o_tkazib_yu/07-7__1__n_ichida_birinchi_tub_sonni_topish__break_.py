n = int(input())
if n < 2:
    print("No")
else:
    i = 2
    while i <= n:
        prime = True
        j = 2
        while j < i:
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime:
            print(i)
            break
        i += 1
        