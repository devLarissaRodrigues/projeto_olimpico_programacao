a = input().split()
b = input().split()
c = input().split()
d = input().split()

list_a = []
list_b = []
list_c = []
list_d = []

for i in range(len(a)):
  i = int(a[i])
  list_a.append(i)
  sum_a = sum(list_a)

for j in range(len(b)):
  j = int(b[j])
  list_b.append(j)
  sum_b = sum(list_b)

for k in range(len(c)):
  k = int(c[k])
  list_c.append(k)
  sum_c = sum(list_c)

for l in range(len(d)):
  l = int(d[l])
  list_d.append(l)
  sum_d = sum(list_d)

list_total_sum = [sum_a, sum_b, sum_c, sum_d]
max_list = max(list_total_sum)


max_binary = "{0:b}".format(max_list)

print(f"{max_list} = {max_binary}")
