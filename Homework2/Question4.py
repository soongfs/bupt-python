from math import sqrt


eps: float = float(input())
pi: float = 0.0
cal: float = float("inf")
cnt: int = 1
while cal > eps:
    cal = 1 / (cnt**2)
    cnt += 1
    pi += cal
print(f"{sqrt(pi * 6):.6f}")
