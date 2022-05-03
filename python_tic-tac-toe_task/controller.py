"""Controller module for tictactoe"""
from os import close
from model import Model
from view_cli import View
from logger import log_



class Controller:
    """controller class"""
    def __init__(self):
        # key_for_xy is dictionary, shows how to interpret input symbols in coordinates
        self.key_for_xy = {
            "q": (0, 0), "w": (0, 1), "e": (0, 2),
            "a": (1, 0), "s": (1, 1), "d": (1, 2),
            "z": (2, 0), "x": (2, 1), "c": (2, 2),
        }
        self.player = 1  # x goes first
        self.status = None
        self.players_names, self.champions = [], {}
        self.championship_flag = False
        self.view = View()  # the view
        self.model = None
        self.start_page()

    def start_page(self):
        """menu page controller"""
        menu_selector = self.view.show_menu()
        if menu_selector == '1':
            self.start()
        elif menu_selector == '2':
            self.view.reader()
            self.start_page()
        elif menu_selector == '3':
            with open('ttt.txt', 'w', encoding='utf-8') as wins_file:
                wins_file.close()
            self.start_page()
        else:
            close(0)

    def start(self):
        """starts a game, asks names and other"""
        while True:
            self.names_admin()
            self.model = Model()  # init game field
            self.status = self.model.check_win()
            while self.status == 0:  # nobody won, no draw
                self.view.render(self.model)
                turn = self.view.get_turn(self.player, self.players_names)
                while not self.move(turn):
                    turn = self.view.get_turn(self.player, self.players_names, error=True)
                self.status = self.model.check_win()

            self.view.render(self.model)
            self.results()
            self.view.wait_for_enter()
            self.start_page()

    def results(self):
        """results print controller"""
        if self.championship_flag:
            log_.warning(self.this_championship())

        else:
            self.view.the_end(self.status, self.players_names)
            self.make_log_win()

    def move(self, key):
        """each next move controller"""
        if key in self.key_for_xy:
            if self.model.get(self.key_for_xy[key]) != 0:
                return False
            self.model.set(self.key_for_xy[key], self.player)
            self.player = 3 - self.player
            return True
        return False

    def names_admin(self):
        """names administrator or 'Do you want to rewrite players names?'
        also administrates championship flag"""
        if not self.players_names:
            self.new_names_now()
        else:
            if self.view.is_need_to_rewrite() == '1':
                self.new_names_now()
            else:
                self.championship_flag = True
                self.this_championship()

    def new_names_now(self):
        """immediately generates new names"""
        self.players_names = [self.view.player_name(1), self.view.player_name(2)]
        self.champions = {self.players_names[0]: 0, self.players_names[1]: 0}

    def this_championship(self):
        """administrates points of champions"""
        if self.status == 1:
            self.champions[self.players_names[0]] += 1
        elif self.status == 2:
            self.champions[self.players_names[1]] += 1
        else:
            pass
        return self.view.championship(self.players_names, self.champions)

    def make_log_win(self):
        """load game results into log(ttt.txt)"""
        # ttt equals to Tic Tac fkn Toe
        if self.status == 1:
            text = self.players_names[0] + " wins"
        elif self.status == 2:
            text = self.players_names[1] + " wins"
        else:
            text = self.players_names[0] + ' draw ' \
                      + self.players_names[1]
        log_.warning(text)
