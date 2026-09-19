matn = input().lower()

unli_soni = (
    matn.count("a")
    + matn.count("e")
    + matn.count("i")
    + matn.count("o")
    + matn.count("u")
)
print(unli_soni)