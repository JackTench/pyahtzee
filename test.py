import player as p
import score as s

import logger

player = p.Player("")

logger.initLog()
logger.log("Test")

# Roll dice and print score in ones.
dice = player.roll()
print(str(dice))

s.printScores(dice)