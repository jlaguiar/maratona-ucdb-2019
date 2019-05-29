n = int(input())
v = []
for i in range(2000):
    v.append(0)

while n != 0:
    v[int(input()) - 1] += 1
    n -= 1

for i in range(2000):
    if (v[i] > 0):
        print(i + 1, "aparece", v[i], "vez(es)")