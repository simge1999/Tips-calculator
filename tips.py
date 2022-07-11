bill = 20
tip_calculater = 0.15
tax_percentage = 0.067
print(f"Bill: {bill}")
tip = bill * tip_calculater
print(f"Tip:{tip}")
tax = bill * tax_percentage
print(f"Tax: {tax}")
total = bill + tip + tax
print(f"Total: {total}")