
p1 = raw_input("PLAYER 1: (r=ROCK, p=PAPER, s=SCISSORS) > ")
p2 = raw_input("PLAYER 2: (r=ROCK, p=PAPER, s=SCISSORS) > ")

if p1 == "r" and p2 == "s":
  print "Player 1 wins!"
elif p1 == "p" and p2 == "r":
  print "Player 1 wins!"
elif p1 == "s" and p2 == "p":
  print "Player 1 wins!"
elif p1 == p2:
  print "Draw!"
else:
  print "Player 2 wins!"
