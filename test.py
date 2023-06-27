import player as p
import score as s

player = p.Player("")

# Roll dice and print score in ones.
dice = player.roll()
print(str(dice))

score = s.ones(dice)
print("Ones: " + str(score))

score = s.twos(dice)
print("Twos: " + str(score))