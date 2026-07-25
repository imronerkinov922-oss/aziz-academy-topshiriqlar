# Musobaqa: kunlik hisobot
# Kurs: Dasturlash / IT
# Mavzu: Arifmetik operatorlar — + - * / // % ** va prioritet
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
tushum, jami_soni, max_t = 0, 0, -1
best_nom = ""

for _ in range(n):
    nom, narx, soni = input().split()
    t = int(narx) * int(soni)
    tushum += t