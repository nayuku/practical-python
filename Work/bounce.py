# bounce.py
#
# Exercise 1.5
height = 100
bounce_ratio = 3/5

for i in range(10):
  height *= bounce_ratio
  print(f"{i+1} {round(height, 4)}")
