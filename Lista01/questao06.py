salary = float(input())

if salary >= 0 and salary <= 400:
  percentual = 15
  money_earned = salary * 0.15
  new_salary = salary + money_earned
elif salary >= 400.01 and salary <= 800:
  percentual = 12
  money_earned = salary * 0.12
  new_salary = salary + money_earned
elif salary >= 800.01 and salary <= 1200:
  percentual = 10
  money_earned = salary * 0.10
  new_salary = salary + money_earned
elif salary >= 1200.01 and salary <= 2000:
  percentual = 7
  money_earned = salary * 0.07
  new_salary = salary + money_earned
elif salary > 2000:
  percentual = 4
  money_earned = salary * 0.04
  new_salary = salary + money_earned


print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {money_earned:.2f}")
print(f"Em percentual: {percentual} %")