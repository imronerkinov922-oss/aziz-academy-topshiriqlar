s = 0
c = 0
while True:
    x = int(input())
    if x == 0:
        break
    s += x
    c += 1
if c == 0:
    print(0)
else:
    print(s/c)
    
        