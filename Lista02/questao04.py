# Charlie is working on decorating a June party and needs several spheres to decorate the garden. He finds wooden spheres, but needs to paint them in the party's theme colors, which are: red ("vermelho"), blue ("azul") and yellow ("amarelo"). The spheres are not the same size, and he needs to follow a pattern, in which spheres with a radius smaller than 12 will be red ("vermelho"), between 12 and 15 will be blue ("azul") and spheres with a radius greater than 15 will be yellow ("amarelo"). The square centimeter of red ink costs R$0.09, of blue ink the corresponding value is R$0.07 and for yellow ink the value is R$0.05 for each square centimeter. Based on the area described on the spheres' packaging, Charlie needs to know what ink he should paint them with and what the cost of each ink will be.

# Note: For this problem, consider π = 3.14.
import math

cases = int(input())
spheres_list = []
radius_list = []

for i in range(cases):
  spheres_list.append(int(input()))
  radius = math.sqrt(spheres_list[i]/3.14)
  radius_list.append(radius)

# for j in range(len(radius_list)):
#   if j < 12:
#     red = radius_list[j]
#   elif j >= 12 and j <= 15:
#     blue = radius_list[j]
#   else:
#     yellow = radius_list[j]

print(f"red= {red}")
print(f"blue= {blue}")
print(f"yellow= {yellow}")
# 3629
# 1519
# 2122