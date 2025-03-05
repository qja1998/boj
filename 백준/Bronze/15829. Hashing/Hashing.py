n = input()
s = input()
start = ord('a') - 1
ans = 0
for i, c in enumerate(s):
	ans += (ord(c) - start) * (31 ** i)
	ans %= 1234567891
print(ans)