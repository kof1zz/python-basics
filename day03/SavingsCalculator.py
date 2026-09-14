salary = int(input("Enter your monthly salary: "))
expenses = int(input("Enter your monthly expenses: "))

monthly_savings = salary-expenses
potential_yearly_savings = monthly_savings*12

print(f"Monthly savings: {monthly_savings}")
print(f"Potential yearly savings: {potential_yearly_savings}")