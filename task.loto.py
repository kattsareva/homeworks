import random
import sys
import time

class Tub:
    def a(self):
        lst = [x for x in range(1, self.amount + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('{:*^30}'.format('*'))
            print('New tub is {} ({} left)'.format(y, self.amount - (i + 1)))
            yield y

    def __init__(self, amount):
        self.amount = amount
        self.gen = self.a()

class Loto:
    def __set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_row != 0:
            cards.append('None')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_owner = cards[:3]
        self.card_c = cards[3:]

    def __init__(self, amount_card):
        row = 3
        self.all_row = row * amount_card
        self.__set_card()

    def get_card(self, player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]}'.format(player[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]}'.format(player[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]}'.format(player[2]))
        print('{:-^25}'.format( '-'))

    def search(self, player, n_tub):
        for i, n in enumerate(player):
            if n_tub in n:
                player[i][n.index(n_tub)] = '-'
                self.score += 1
                if self.score == 15:
                    print('{} wins!'.format(self.name))
                    sys.exit(1)
                return True
            return False

class Player(Loto):
    def __init__(self, name):
        self.name = name
        self.score = 0

def main():
    game = Loto(2)
    tub = Tub(90)
    player_1 = Player('Your card')
    player_2 = Player('Computers card')

    while True:
        n_tub = next(tub.gen)
        player_1.get_card(game.card_owner)
        player_2.get_card(game.card_c)

        inp_owner = input('Cross out? (y/n)')
        if inp_owner == 'y':
            if player_1.search(game.card_owner, n_tub):
                continue
            else:
                print('Game over')
                sys.exit(1)

        if inp_owner == 'n':
            if player_1.search(game.card_owner, n_tub):
                print('Game over')
                sys.exit(1)
            elif player_2.search(game.card_c, n_tub):
                continue

        if inp_owner != 'n' and inp_owner != 'y':
            print('Write y or n')
            time.sleep(1)
            continue

if __name__ == '__main__':
    main()