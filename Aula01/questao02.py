# Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place.

grade1 = float(input(f"Digite a primeira nota: "))
grade2 = float(input(f"Digite a segunda nota: "))
grade3 = float(input(f"Digite a terceira nota: "))

average = ((grade1 * 2) + (grade2 * 3) + (grade3 * 5))/10
print(f"MEDIA = {average:.1f}")