S = input()
a, b = map(int, S.split('x^'))
ans = f"{a*b}x^{b-1}"
print(ans)