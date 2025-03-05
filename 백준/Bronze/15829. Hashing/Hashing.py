n = input()
s = input()
start = ord('a') - 1
ans = 0
for i, c in enumerate(s):
	ans += (ord(c) - start) * (31 ** i)
print(ans)