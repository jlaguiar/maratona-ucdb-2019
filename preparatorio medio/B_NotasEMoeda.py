n = input().split('.')
parte_inteira = int(n[0])
parte_decimal = int(n[1])

n100 = int(parte_inteira/100)
parte_inteira = parte_inteira%100
n50 = int(parte_inteira/50)
parte_inteira = parte_inteira%50
n20 = int(parte_inteira/20)
parte_inteira = parte_inteira%20
n10 = int(parte_inteira/10)
parte_inteira = parte_inteira%10
n5 = int(parte_inteira/5)
parte_inteira = parte_inteira%5
n2 = int(parte_inteira/2)
parte_inteira = parte_inteira%2
print("NOTAS:")
print(n100, "nota(s) de R$ 100.00")
print(n50, "nota(s) de R$ 50.00")
print(n20, "nota(s) de R$ 20.00")
print(n10, "nota(s) de R$ 10.00")
print(n5, "nota(s) de R$ 5.00")
print(n2, "nota(s) de R$ 2.00")

parte_decimal += 100*parte_inteira
m100 = int(parte_decimal/100)
parte_decimal = parte_decimal%100
m50 = int(parte_decimal/50)
parte_decimal = parte_decimal%50
m25 = int(parte_decimal/25)
parte_decimal = parte_decimal%25
m10 = int(parte_decimal/10)
parte_decimal = parte_decimal%10
m5 = int(parte_decimal/5)
parte_decimal = parte_decimal%5
m1 = parte_decimal

print("MOEDAS:")
print(m100, "moeda(s) de R$ 1.00")
print(m50, "moeda(s) de R$ 0.50")
print(m25, "moeda(s) de R$ 0.25")
print(m10, "moeda(s) de R$ 0.10")
print(m5, "moeda(s) de R$ 0.05")
print(m1, "moeda(s) de R$ 0.01")