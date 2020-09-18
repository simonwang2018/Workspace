import random
from cards import Card
#------------使用嵌套for循环建立一副牌
deck = []
for suit_id in range(1,5):
    for rank_id in range(1,14):
        deck.append(Card(suit_id,rank_id))
#----------从一副牌中选5张牌作为一手牌-------------
hand = []
for cards in range (0,5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print()
for card in hand:
    print(card.short_name, '=', card.long_name, 'Value:', card.value)
