import random

numb = random.randint(1,9)
guess = int(raw_input("Pick a number 1-9 > "))

print numb

if guess < numb:
    print "Too low"
elif guess > numb:
    print "Too high"
else:
    print "You're right!"
