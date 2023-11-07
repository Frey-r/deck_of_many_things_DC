import random

cards = {
    "Vizier":"https://i.imgur.com/QvxobgN.jpeg",
    "Sun":"https://i.imgur.com/tSycGHp.jpeg",
    "Moon":"https://i.imgur.com/i2gAky1.jpeg",
    "Star":"https://i.imgur.com/BsoLMba.jpeg",
    "Comet":"https://i.imgur.com/8LOZ0ao.jpeg",
    "The Fates":"https://i.imgur.com/irhPSXk.jpeg",
    "Throne":"https://i.imgur.com/4kThyEt.jpeg",
    "Key":"https://i.imgur.com/2Bnm6wa.jpeg",
    "Knight":"https://i.imgur.com/C2JArKe.jpeg",
    "Gem":"https://i.imgur.com/TAxuknF.jpeg",
    "Talons":"https://i.imgur.com/LhL067C.jpeg",
    "The Void":"https://i.imgur.com/BMktPl3.jpeg",
    "Flames":"https://i.imgur.com/gQWvBhh.jpeg",
    "Skull":"https://i.imgur.com/layNke7.jpeg",
    "Idiot":"https://i.imgur.com/8hR7jxu.jpeg",
    "Donjon":"https://i.imgur.com/TlJSY4J.jpeg",
    "Ruin":"https://i.imgur.com/zDDktr7.jpeg",
    "Euryale":"https://i.imgur.com/M5xras0.jpeg",
    "Rogue":"https://i.imgur.com/I8B5f6Q.jpeg",
    "Balance":"https://i.imgur.com/R7wcXS7.jpeg",
    "Fool":"https://i.imgur.com/rhwhV5L.jpeg",
    "Jester":"https://i.imgur.com/iR8kFV6.jpeg"
}

discard_pile = {}

def deckear():
    if not cards:
        return False
    random_card_name = random.choice(list(cards.keys()))
    random_card_link = cards[random_card_name]
    if (random_card_name != "Fool" and random_card_name != "Jester"):
        discard_pile[random_card_name] = random_card_link
        del cards[random_card_name]
        print(f'{random_card_name} deleted')
    else:
        print(f'{random_card_name} not deleted')


    return f"{random_card_name}"

def discardDeck():
    if not discard_pile:
        return False
    random_card_name = random.choice(list(discard_pile.keys()))
    random_card_link =discard_pile[random_card_name]

    return f"{random_card_name}"