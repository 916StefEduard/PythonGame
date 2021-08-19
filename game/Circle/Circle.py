from termcolor import colored

class Circle:
    """
    The circle class for every player.
    """
    def __init__(self, chosen_color):
        self.__color = chosen_color

    def __str__(self):
        """
        Returns a circle of the color specified
        """
        return colored('⬤', str(self.__color))

