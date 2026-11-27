n = int(input())
jami = 0
for i in range(n):
    nom, narx, soni = input().split()
    summa = int(narx) * int(soni)
    print(f"{nom}: {summa}")
    jami += summa
print(f"Jami: {jami}")