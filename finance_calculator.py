monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annul_savings = monthly_savings * 12
print(f"Projected savings after one year, with interest, is: {annul_savings}")