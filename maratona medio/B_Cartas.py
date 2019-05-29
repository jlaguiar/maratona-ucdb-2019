v = input().split()
c = True
d = True
for i in range(1, 5):
    if (int(v[i]) < int(v[i - 1])):
        c = False
    else:
        d = False

if (c):
    print('C')
elif (d):
    print('D')
else:
    print('N')