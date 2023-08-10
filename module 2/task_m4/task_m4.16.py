#Гра в карти
#Масті:
#s (Spades) Піки
#h (Hearts) Черви
#d (Diamonds) Бубни
#c (Clovers) Хрести
#Створюємо колоду карт
def create_deck():
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = list()
    for suit in suits:
        for value in values:
            deck.append(f'{value}{suit}')
    return deck


from random import randrange

#Перетасуємо карти
def shuffle_deck(deck):
    new_deck = deck.copy()
    for i in range(0, len(deck)):
        other_index = randrange(0, len(new_deck))
        new_deck[i], new_deck[other_index] = new_deck[other_index], new_deck[i]
    return new_deck

#Виконаємо роздачу карт
def deal(players, cards, deck):
    if players * cards > len(deck):
        return deck

    table = list()

    for _ in range(0, cards):
        for player in range(0, players):
            if player >= len(table):
                table.append([deck.pop()])
            else:
                table[player].append(deck.pop())
    return table

#Імітуємо гру
def main(players, cards):

    init_deck = create_deck()
    print(f"Open new deck: {init_deck}")

    deck = shuffle_deck(init_deck)

    print(f"Shuffle deck: {deck}")
    print(f"Invite {players} players to table")
    print(f"Give cards to players ({cards} to one player)")

    table = deal(players, cards, deck)

    for i in range(players):
        print(f"Players №{i+1} has cards: {table[i]}")

    print(f"Deck in the final {deck}")


if __name__ == '__main__':
    main(4, 6)