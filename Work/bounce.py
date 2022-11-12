# bounce.py
#
# Exercise 1.5

INIT_HEIGHT = 100
FADING = 3 / 5

number_of_bounces = int(input('Input number of bounces: '))
h = None

for i in range(1, number_of_bounces + 1):
     if not h:
         h = INIT_HEIGHT
    
     h *= FADING
     print(i, round(h, 4))
