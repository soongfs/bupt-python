from math import isqrt


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, isqrt(x) + 1, 2):
        if x % i == 0:
            return False
    return True


x = int(input())
ans = []
while x > 1:
    for i in range(2, x + 1):
        if x % i == 0 and is_prime(i):
            ans.append(i)
            x //= i
            break
print(",".join(map(str, ans)))

# 很不优雅，懒得改了
