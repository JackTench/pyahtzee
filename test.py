import player
import score

p = player.Player("test")

roll = p.roll()
s = score.scoreDice(roll)
p.score(0, roll)
score = p.getTotalScore()
print(score)
