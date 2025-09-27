from collections import defaultdict

num = input()
cnt = defaultdict(int)
for digit in num:
    cnt[digit] += 1

for i in range(10):
    print(i, ":", cnt[str(i)])
