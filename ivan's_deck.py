def deck_shuffled():      ## Понятно что подчеркнуто, мол не может он из другой 
    random.shuffle(deck)  # функции узнать что такое DECK. Как это решить? Создать еще DECK? 
    return deck_shuffled  #Но будут проблемы с двумя разными переменными, которые названы одинаково??
                          ## Как между собой связано то, что в скобках у DEF, и то что в RETURN


deck_shuffled # единообразие называния переменных и функций достигается тем, что в начале пишется ЧТО, а затем В КАКОМ СОСТОЯНИИ.
              # Или позже я еще что-то пойму про классы и голова не будет болеть)

del shufled_deck[0:1] # удаляет 2е первые карты из списка

list(player_1) # 1ый список,хранящий значения 3х элементов карты, которые "выятнул" 1 ый игрок
player_1 = 
list(player_2) # 2ой список,хранящий значения 3х элементов(value) карты(card), которые "выятнул" 2 ой игрок

random.choice(deck_shuffled)

# а есть 

random.choices()

# еще есть неглубокое копирование(((((((
# Но нам не нужен весь объект, а нужен не третий аргумент, а третий элемент из туплета из списка.
# Т.Е. создавать новый список из карт не надо. Надо сравнить сумму третьих элементов.


    
# Вот есть колода из 52 карт. Мы из нее рандомно достанем половину карт, это 26 штук.
# Дай мне сумму половины карт, которые были случайно выбраны.
# Дай мне сумму 3их элементов туплетов

# 