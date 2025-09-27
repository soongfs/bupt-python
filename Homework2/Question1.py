cost: int = int(input())
if cost >= 35:
    cost -= 12
elif cost >= 20:
    cost -= 8
if cost >= 50:
    print(cost)
elif cost >= 30:
    print(cost + 5)
else:
    print(cost + 10)
