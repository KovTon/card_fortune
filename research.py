def choose_data_structure_for_card():

    card_str_1 = "Q♣12"
    card_str_2 = "6♥6"
    card_str_3 = "A♣14"

    # card_tuple_1 = ("Q", "♣", 12)
    # card_tuple_2 = ("6", "♥", 6)

    print(card_str_1 == card_str_2)
    print(card_str_1 > card_str_2)
    print(card_str_1 < card_str_2)
    print('*********')
    print(card_str_1 == card_str_3)
    print(card_str_1 > card_str_3)
    print(card_str_1 < card_str_3)

    print(card_str_1[0:2])
    print(card_str_2)
    print(card_str_3)


dangeon = [[[]], [[], []], [[], [[]], []]]


player_1 = {
    'name': 'Ivan',
    'score': 500,
    'date': '16.03.2023',
    'place': 1
}

player_2 = {
    'name': 'Pavel',
    'score': 500,
    'date': '17.03.2023',
    'place': 1
}

print(player_1)
# print(player_1[name])
print(player_1['name'])
print(player_2['name'])
