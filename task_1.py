import random
import os


class LotoGame:

    def __init__(self):
        self.my_list = []
        self.total_list = [i for i in range(1, 91)]
        random.shuffle(self.total_list)
        self.game_over = False

    def show_card(self):
        print('Карточка игрока: ', self.name)
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                print("%3s" % self.my_list[i][j], end='|')
            print()

    def next_number(self):
        for i in range(0, 90):
            yield self.total_list[i]

    def step(self, player_card, computer_card):
        for ind, el in enumerate(self.next_number(), 1):
            next_step = el
            count = 0
            total_plus_player = 0
            total_plus_computer = 0
            print(f'Выпал бочонок номер: {next_step} (осталось {90 - ind} бочонков)')
            player_card.show_card()
            print()
            computer_card.show_card()
            choice = input("Вычеркнуть цифру? (y/n): ")
            if choice == 'y':
                for i in range(len(player_card.my_list)):
                    for j in range(len(player_card.my_list[i])):
                        if player_card.my_list[i][j] == next_step:
                            player_card.my_list[i][j] = '+'
                        else:
                            count += 1
                if count == 27:
                    print('Такой цифры нет в вашей карточке. Вы проиграли!')
                    self.game_over = True
                    break
            elif choice == 'n':
                for i in range(len(player_card.my_list)):
                    for j in range(len(player_card.my_list[i])):
                        if player_card.my_list[i][j] == next_step:
                            count = 1

                if count == 1:
                    print('Такая цифра есть в вашей карточке. Вы проиграли!')
                    self.game_over = True
                    break
            else:
                print("Неверный символ. вы проиграли!")
                self.game_over = True
                break

            for i in range(len(computer_card.my_list)):
                for j in range(len(computer_card.my_list[i])):
                    if computer_card.my_list[i][j] == next_step:
                        computer_card.my_list[i][j] = '+'

            for i in range(len(player_card.my_list)):
                for j in range(len(player_card.my_list[i])):
                    if player_card.my_list[i][j] == '+':
                        total_plus_player += 1

            for i in range(len(computer_card.my_list)):
                for j in range(len(computer_card.my_list[i])):
                    if computer_card.my_list[i][j] == '+':
                        total_plus_computer += 1

            if total_plus_player == 15:
                print("Вы выиграли")
                self.game_over = True
                break

            elif total_plus_computer == 15:
                print("Выиграл компьютер")
                self.game_over = True
                break

            elif total_plus_player == total_plus_computer and total_plus_player == 15:
                print("Ничья")
                self.game_over = True
                break

            print('\n')

class LotoCard(LotoGame):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def create_card(self):
        for i in range(3):
            self.my_list.append([])
            for j in range(9):
                self.my_list[i].append('')
        my_set = set()
        count = 0
        i = 0
        while count < 15:
            while i < 3:
                new_elem = random.randint(1, 90)
                x = len(my_set)
                my_set.add(new_elem)
                if len(my_set) != x:
                    if new_elem == 90 and self.my_list[i][new_elem // 10 - 1] == '':
                        self.my_list[i][new_elem // 10 - 1] = new_elem
                        count += 1
                    if new_elem == 90 and self.my_list[i][new_elem // 10 - 1] != '':
                        continue
                    if self.my_list[i][new_elem // 10] == '':
                        self.my_list[i][new_elem // 10] = new_elem
                        count += 1
                    if count % 5 == 0:
                        i += 1

lotogame = LotoGame()
player_card = LotoCard('Nik')
computer_card = LotoCard('Computer')
player_card.create_card()
computer_card.create_card()

while not lotogame.game_over:
    lotogame.step(player_card, computer_card)
