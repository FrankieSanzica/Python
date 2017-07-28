print "You see a lawn gnome standing between 2 doors.  His hand points towards door 2.  Which door do you choose?"

door = raw_input("> ")

if door == "1":
    print "You see a giant squirrel racing towards you."
    print "1. Scream and run away, arms flailing."
    print "2. Stand your ground and clench your fists"

    squirrel = raw_input("> ")

    if squirrel == "1":
        print "The squirrel catches you.  You become part of his accorn collection."
        print "GAME OVER!"
    elif squirrel == "2":
        print "The squirrel drops his accorn and flees in terror."
        print "GAME OVER!"

elif door == "2":
    print "You enter a garden, with 3 lawn ornaments.  Which do you chose?"
    print "1. The lawn gnome"
    print "2. Plastic flamingo"
    print "3. Bird bath"

    garden = raw_input("> ")

    if garden == "1":
        print "The lawn gnome's eyes glow, turning you into a golden lawn gnome.  You guard the garden for enternity IN GOLD!"
        print "GAME OVER!"
    elif garden == "2":
        print "The flamingo pecks your eyes out!"
        print "GAME OVER!"
    elif garden == "3":
        print "The bird bath is much bigger than expected, you paddle for as long as you can before dying."
        print "GAME OVER!"
