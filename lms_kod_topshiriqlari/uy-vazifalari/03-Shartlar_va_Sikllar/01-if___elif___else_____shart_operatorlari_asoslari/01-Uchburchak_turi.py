a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    print('teng tomonli' if a == b == c else 'teng yonli' if a == b or a == c else 'turli tomonli')
else:
    print('notogri')
    