salary = float(input("Enter your salary: "))
months = int(input("Enter how many months you've worked: "))

#21% taxes
taxes = 0.21 
  
annual_income = round((salary*months)*taxes,2)

print(f"Your annual income {annual_income}")
