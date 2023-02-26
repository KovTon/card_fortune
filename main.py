from typing import List, Tuple
import random

Card = Tuple[str, str, int]


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


def pull_random_card(deck) -> Card:
    card_index = random.randint(0, len(deck)-1)
    card = deck.pop(card_index)
    return card


def cards_are_equal(card_1: Card, card_2: Card) -> bool:
    return card_1[2] == card_2[2]


def start_round(deck, player_1, player_2):
    player_1_card = pull_random_card(deck)
    player_2_card = pull_random_card(deck)
    # 64 строка была 1-4 главах? =
    if cards_are_equal(player_1_card, player_2_card):
        return

    if player_1_card[2] > player_2_card[2]:
        player_1.append(player_1_card)
    else:
        player_2.append(player_2_card)


def introduce_game(deck):
    print(f'вы играете колодой из {len(deck)} карт')


def start_game_loop(deck, player_1, player_2):
    while deck:  # неявная конвертацияиз list в bool. Явная когда вызвали
        start_round(deck, player_1, player_2)


def show_results(player_1, player_2):
    print(len(player_1), len(player_2))


def anounce_winner(player_1, player_2):
    if len(player_1) == len(player_2):
        print("draw")
    elif len(player_1) > len(player_2):
        print("winner-player 1")
    else:
        print("winner-player 2")


def main():
    player_1 = []
    player_2 = []
    deck = generate_standart_deck()
    random.shuffle(deck)
    introduce_game(deck)
    start_game_loop(deck, player_1, player_2)
    anounce_winner(player_1, player_2)
    show_results(player_1, player_2)


if __name__ == '__main__':
    main()
