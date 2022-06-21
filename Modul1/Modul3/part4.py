income = float(input("Enter the annual income: "))

if income < 85.528:
    tax_relief: float = income * 18 / 100 - 556.2
elif income > 85.828:
    tax_relief: float = 14839.2 + (85.528 * 32 / 100)
else:
    tax_relief = 0
    tax_relief = round(tax_relief, 0)
print("The tax is:", tax_relief, "thalers")

