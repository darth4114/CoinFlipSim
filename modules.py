import random


def coin_flip():
    '''	Flips a coin, heads or tails. Takes no input'''
    flip = random.randint(0, 1)

    if flip:
        return "Heads"
    else:
        return "Tails"


def ask():
    '''	Asks for an integer value for how many times to flip a coin'''
    while True:
        try:
            tries = int(
                input("\nHow many times would you like to flip the coin? "))
        except:
            print("Sorry, I did not understand you\n")
            continue
        else:
            break

    return tries


def flip_count(flips):
    '''
    Counts the instances of heads and tails over x amount of flips
    args = number of flips
    '''

    heads = 0
    tails = 0

    for i in range(flips):
        if coin_flip() == "Heads":
            heads += 1
        else:
            tails += 1

    return heads, tails
