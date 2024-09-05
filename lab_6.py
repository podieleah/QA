# Part 1

def get_income_tax(salary):
  personal_allowance = 11850

  if salary <= personal_allowance:
    return 0
  elif salary <= 34500:
    taxable_income = salary - personal_allowance
    return taxable_income * 0.20
  elif salary <= 150000:
    taxable_income = salary - personal_allowance
    basic_tax = 34500 * 0.20
    higher_rate_tax = (taxable_income - 34500) * 0.40
    return basic_tax + higher_rate_tax
  else:
    taxable_income = salary - personal_allowance
    basic_tax = 34500 * 0.20
    higher_rate_tax = (150000 - 34500) * 0.40
    additional_rate_tax = (taxable_income - 150000) * 0.45
    return basic_tax + higher_rate_tax + additional_rate_tax

def main():
  salary = float(input("Enter your salary: "))
  income_tax = get_income_tax(salary)
  print("Your income tax is: £", income_tax)

main()