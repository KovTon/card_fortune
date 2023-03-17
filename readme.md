# Партейку в картейку

Нужно написать карточную игру.

- [x] В ней есть два игрока и колода карт.
- [x] Колода карт должна быть перемешана.
- [x] Каждый игрок по очереди вытаскивает рандомную карту из колоды.
- [x] Затем ироки сравнивают карты между собой.
- [x] Большая карта побеждает в раунде, тот кто ее вытащил забирает себе.
- [X] Когда карт не останется подводят итог кто был более удачливый.

## Какие сущности нам нужны?

- 2 игрока,
- 1 колода карт,
- 52 карты,
- раунд,
- игра.

## Какими типами данных мы будем их представлять?

### Игрок

Это хранитель очков.
Имена им уже присвоены
(Имена: игрок 1, игрок 2)
Тип данных: список (Имя, кол-во очков)

### Колода карт

Это набор карт.
  Требавния:
 1)Возможность перемешивать карты.
 2)Можно удалять карты из колоды.(Выбрали)
  Тип данных: список

### Карта

Объект с двуми характеристиками: масть и значение.

  Требования:

- 1)Должен содержать один тип данных.
- 2)Они должны быть сраваемые.
  Карта может иметь величину от 2 до 14.
  2 < 14
  2 == 2
  14 > 2
- 3)Они должны отображаться в консоли.
  Q♠, 4♦, A♥, 6♣.
- 4)Карта должна быть не изменяема.(если 2 туза пик появится,
игра провалится)

  Тип данных:
кортеж

``` py
card = (Q, ♣, 12)
Q♣ = 12, 6♥ = 6.
```

   Раунд:
       Это набор действий игроков и игры.
           Игрок_1 берет карту
           Игрок_2 берет карту
              deck.random()
              0 1
           Игра сравнивает карты
           Игра начисляет очко победителю
           Раунд закончен
           Игрок 1 берет карту ....
   Игра:
       32 раунда сравнеий рандомных пар карт и
       присвоение звания Лаки-плеера.

Где хранить результаты раундов?
  В игроках.
Как показывать раунд?
  
Как показывать карт?
  Пользователь будет видеть строчку типа: "..."
Как сравнивать карты?
  2 3 4 5 6...2 3 4 5 6...13 14 15
  0 1 2 3 4...17
Как карты будут выбывать из колоды?
  
Как предлагать выбирать карты?
