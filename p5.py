# random card

import random

card=["spades","clubs","diamond","hearts"]

ranks=[1,2,3,4,5,6,7,8,9,10,"jack","Queen","King","Ace"]

def rand_card():

    random_card=random.choice(card)
    random_ranks=random.choice(ranks)

    print(f"The[{rand_card}] of [{random_ranks}]")

rand_card()
