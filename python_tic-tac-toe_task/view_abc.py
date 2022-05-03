"""module for abstract view scratch"""
from abc import ABC, abstractmethod


class ViewABC(ABC):
    """abstract view class-scratch"""
    @staticmethod
    def show_menu():
        """menu printer"""

    @staticmethod
    def player_name(pl_no):
        """ask and return player`s name"""

    @staticmethod
    def is_need_to_rewrite():
        """return 'rewrite is needed?'"""

    @abstractmethod
    def decode_row(self, row):
        """prints 1 row"""

    def render(self, field):
        """render view of game"""

    @staticmethod
    def get_turn(who, players, error=False):
        """input validator"""

    @staticmethod
    def the_end(status, players):
        """result printer"""

    @staticmethod
    def championship(players, champions):
        """result printer for championship"""

    @staticmethod
    def wait_for_enter():
        """waits for enter to continue"""

    @staticmethod
    def reader():
        """read file with previous statistics"""
