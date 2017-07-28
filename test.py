#!/usr/bin/env python

import sys

## Sort list with 0's at the end
test = [0, 5, 3, 1, 2, 4, 0]
test = sorted(test)
for number in test:
    if number == 0:
       test.append(test.pop(0))
print test

### Creating classes
class Zombie:
    def __init__(self, size, color, speed):
        self.size = size
        self.color = color
        self.speed = speed

garth = Zombie("small","red","slow")

print garth.size + " " +  garth.color + " " + garth.speed


#EVEN or ODD
ask = raw_input("Enter a Number:  > ")

number = int(ask)

if number % 2 == 0:
    eoa = "EVEN"
else:
    eoa = "ODD"

print "Your number: %d which is %s!" % (number,eoa)

#Less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for number in a:
    if number > 5:
        a.remove(number)
    else:
        print a
