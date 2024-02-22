import random #or we can write specific function call like "from random import random"
import statistics

coin = random.choice(["Head","Tail"])
ranInt = random.randint(1,10)
#for suffle method
cards = ["Ace", "2", "3", "4", "5", "6","7", "8", "9" ,"10", "Jack", "Queen", "King"]
random.shuffle(cards)
print("Suffled cards:")
for card in cards:
    print(card)
print( "Random choice form coin:", coin)
print("Random number from 1 to 10:",ranInt)

#use of statistics
print("\n\nMean of 100 and 500 is :",statistics.mean([100,500]))

