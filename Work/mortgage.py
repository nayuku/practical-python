# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
total_paid = 0.0
payment = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
actual_month = 0

while principal > 0:
  actual_month += 1
  actual_payment = payment  # normal payment
  if extra_payment_start_month <= actual_month <= extra_payment_end_month:  # higher payment
    actual_payment += extra_payment

  principal = principal * (1 + rate / 12) - actual_payment

  # last payment
  if principal < 0:
    actual_payment += principal
    principal = 0

  total_paid += actual_payment
  print(f'{actual_month:<3} {total_paid:>10.2f} {principal:>10.2f}')

print('Total paid:  ', round(total_paid, 2))
print('Months:  ', actual_month)
# print(dir(actual_month))
