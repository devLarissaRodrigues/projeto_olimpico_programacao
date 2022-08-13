# Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

# value = float(input())
# #Ex: 576.73

# integer_value = int(value // 1)
# float_value = f"{value-integer_value:.2f}"
# float_value1 = float(float_value)

# count100 = 0
# count50 = 0
# count20 = 0
# count10 = 0
# count5 = 0
# count2 = 0

# if integer_value % 100 == 0:
#   count100 += 1
# elif integer_value % 50 == 0:
#   count50 += 1
# elif integer_value % 20 == 0:
#   count20 += 1
# elif integer_value % 10 == 0:
#   count10 += 1
# elif integer_value % 5 == 0:
#   count5 += 1
# elif integer_value % 2 == 0:
#   count2 += 1

# print("NOTAS:")
# print(f"{count100} nota(s) de R$ 100.00")
# print(f"{count50} nota(s) de R$ 50.00")
# print(f"{count20} nota(s) de R$ 20.00")
# print(f"{count10} nota(s) de R$ 10.00")
# print(f"{count5} nota(s) de R$ 5.00")
# print(f"{count2} nota(s) de R$ 2.00")