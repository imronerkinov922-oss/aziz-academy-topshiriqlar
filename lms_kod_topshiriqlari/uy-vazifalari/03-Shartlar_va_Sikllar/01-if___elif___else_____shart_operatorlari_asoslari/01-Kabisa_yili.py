yil = int(input())
print(
    "kabisa"
    if (yil % 4 == 0 and yil % 100 != 0) 
    or (yil % 400 == 0)
    else "oddiy"
)


