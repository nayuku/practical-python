# pcost.py
#
# Exercise 1.27
total = 0
with open('Data/portfolio.csv', 'rt') as file:
  headers = next(file)
  for line in file:
    row = line.strip().split(',')
    total += int(row[1])*float(row[2])

print(f'Total cost is {total}')
### reading gzip
import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
  for line in f:
    print(line, end='')
