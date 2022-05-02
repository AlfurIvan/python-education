"""console View module"""
from view_abc import ViewABC


class View(ViewABC):
    """console View class"""
    num2sym = {
        0: "_",
        1: "X",
        2: "O",
    }

    @staticmethod
    def show_menu():
        """menu printer"""
        print('Choose your action:\n'
              '1 - Play\n'
              '2 - Show results table\n'
              '3 - Clear results table\n'
              'Else - Exit\n')
        return str(input())

    @staticmethod
    def player_name(pl_no):
        """ask and return player`s name"""
        return str(input(f'Enter name for player {pl_no}: '))

    @staticmethod
    def is_need_to_rewrite():
        """return 'rewrite is needed?'"""
        return str(input("Do u want to rewrite names?(1)\n"
                         "Continue championship(else)"))

    def decode_row(self, row):
        """prints 1 row"""
        output = ""
        for i in row:
            output += self.num2sym[i] + " "
        return output

    def render(self, field):
        """render view of game"""
        print('\n'*25)
        for i in range(3):
            print(self.decode_row(field.get_row(i)))

    @staticmethod
    def get_turn(who, players, error=False):
        """input validator"""
        if error:
            print("Incorrect input!")
        if who == 1:
            return input(f"{players[0]} goes:")
        return input(f"{players[1]} goes:")

    @staticmethod
    def the_end(status, players):
        """result printer"""
        if status == 1:
            message = players[0] + " wins"
        elif status == 2:
            message = players[1] + " wins"
        else:
            message = "Draw"
        print(message)
        return message

    @staticmethod
    def championship(players, champions):
        """result printer for championship"""
        print(f"Goals between\n"
              f'{players[0], champions[players[0]]} :'
              f' {players[1], champions[players[1]]}')
        return f'{players[0], champions[players[0]]} :' \
               f' {players[1], champions[players[1]]}'

    @staticmethod
    def wait_for_enter():
        """waits for enter to continue"""
        input('\nPress Enter to continue\n')

    @staticmethod
    def reader():
        """read file with previous statistics"""
        with open('ttt.txt', 'r', encoding='utf-8') as wins_file:
            print(wins_file.read())
