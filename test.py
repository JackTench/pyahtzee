import player as p
import score as s

player = p.Player("")

# Roll dice and print score in ones.
dice = player.roll()
print(str(dice))

print(s.threeOfAKind(dice))