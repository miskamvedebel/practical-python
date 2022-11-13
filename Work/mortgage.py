# mortgage.py
#
# Exercise 1.7
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 1

while principal > 0:
    
    # checking for the last payment to not overpay
    if principal * (1+rate/12) <= payment:
        payment = principal * (1+rate/12)

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if month <= extra_payment_end_month and month >= extra_payment_start_month:
        principal -= extra_payment
        total_paid += extra_payment
    month += 1

    print(f'month: {str(month): >5s}, total paid: {str(round(total_paid, 2)): >5s}, total debt left: {str(round(principal, 2)): >5s}')

print('Total paid', total_paid)
print('Total months', month)