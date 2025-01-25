import os


class Utils:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
