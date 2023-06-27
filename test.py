import player as p
import score

player = p.Player("")

# Roll dice and print score in ones.
dice = player.roll()
print(str(dice))

score = score.ones(dice)
print(str(score))