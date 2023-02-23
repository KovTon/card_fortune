from typing import List
import random


def get_grade(number: int):
    grades = {11: "V", 12: "Q", 13: "K", 14: "A"}
    if number in grades:
        return grades[number]
    return str(number)


def generate_deck(suits: List[str], values: List[int]):
    deck = []
    for suit in suits:
        for value in values:
            card = (get_grade(value), suit, value)
            deck.append(card)
    return deck


def generate_standart_deck():
    suits = ["♠", "♦", "♥", "♣"]
    values = list(range(2, 15, 1))
    deck = generate_deck(suits, values)
    return deck


def generate_single_suite_deck():
    suits = ["♠"]
    values = list(range(2, 15, 1))
    deck = generate_deck(suits, values)
    return deck


def generate_double_suite_deck():
    suits = ["♠", "♦"]
    values = list(range(2, 15, 1))
    deck = generate_deck(suits, values)
    return deck


player_1 = []
player_2 = []
deck = generate_standart_deck()
random.shuffle(deck)
print(len(deck))

while len(deck) > 0:
    card_index = random.randint(0, len(deck)-1)
    player_1_card = deck.pop(card_index)
    card_index = random.randint(0, len(deck)-1)
    player_2_card = deck.pop(card_index)

    if player_1_card[2] > player_2_card[2]:
        player_1.append(player_1_card)
    elif player_1_card[2] < player_2_card[2]:
        player_2.append(player_2_card)

print(len(player_1), len(player_2))


print(len(deck))






# for i in range(26):
#     draw = random.choice(deck)
#     player_1.append(draw)
#print(player_1)
#print(len(player_1))
#player_2 = []
#player_2 = 
#print(player_2)
