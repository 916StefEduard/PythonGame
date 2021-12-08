
class Player:
    """
    Initializes the player class so each player can have a circle.
    """
    def __init__(self,circle):
        self.__circle = circle

    def get_circle(self):
        return self.__circle

    def __str__(self):
        return  str(self.__circle)
