def soma_lista(lista):
  numbers = []
  for i in range(len(lista)):
    i = int(lista[i])
    numbers.append(i)
  
  soma = sum(numbers)
  return soma

# Outra forma de transformar lista em inteiro: 
# lista = [int(i) for i in input().split()]
a = input().split()
b = input().split()
c = input().split()
d = input().split()

list_total_sum = [soma_lista(a), soma_lista(b), soma_lista(c), soma_lista(d)]
max_list = max(list_total_sum)

print(list_total_sum)

max_binary = bin(max_list)[2:]
print(f"{max_list} = {max_binary}")

#Exemplo de entrada:
# 24 23 14 15 28 29 54
# 74 15 63 87 95 12 11
# 17 18 15 20 67 36 24
# 14 12 15 87 36 25 47

#Saída esperada:
#357 = 101100101
