result = (sum([int(i) for i in input().split()]) - 1)% 9
if result == 0:
    print("Dasher")
elif result == 1:
    print("Dancer")
elif result == 2:
    print("Prancer") 
elif result == 3:
    print("Vixen")
elif result == 4:
    print("Comet")
elif result == 5:
    print("Cupid")
elif result == 6:
    print("Donner")
elif result == 7:
    print("Blitzen")
else:
    print("Rudolph")