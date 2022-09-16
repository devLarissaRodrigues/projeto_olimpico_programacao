product1 = input().split()
product2 = input().split()

unit1 = int(product1[1])
price1 = float(product1[2])
value1 = unit1 * price1

unit2 = int(product2[1])
price2 = float(product2[2])
value2 = unit2 * price2

total = value1 + value2

print(f"VALOR A PAGAR: R$ {total:.2f}")

