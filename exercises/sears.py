bill_thickness = 0.11 * 0.001
sears_height = 442
num_bills = 1

day = 1

while num_bills * bill_thickness < sears_height:
  print(day, num_bills, num_bills * bill_thickness)
  day += 1
  num_bills *= 2

print(f'Number of days {day}')
print(f'Number of bills {num_bills}')
print(f'Final height {num_bills * bill_thickness}')