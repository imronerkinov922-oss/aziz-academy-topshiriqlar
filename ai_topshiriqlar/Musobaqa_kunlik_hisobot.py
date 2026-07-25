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
    jami_soni += int(soni)
    if t > max_t:
        max_t, best_nom = t, nom
            
print(tushum)
print(best_nom)
print(jami_soni)