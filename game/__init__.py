from typing import List

class Field:
    def __init__(self):
        pass

    def getFields(self) -> List:
        pass

    def setFields(self, col: int, value: int):
        pass

    def getLastRow(self, col: int, row: int) -> int:
        pass

    def getLastCol(self) -> int:
        pass

class GUI:
    def __init__(self):
        pass

    def outputField(self, field: Field):
        pass

    def getName(self, playerNr: int) -> str:
        pass

    def getGameMode(self, name: str) -> int:
        pass

    def getDraw(self, name: str) -> Position:
        pass

class Player:
    def __init__(self, name: str, playerid: str,  gameMode: int):
        self.__name = name
        self.__playerid = playerid
        if gameMode == 1 or gameMode == 2: #Erzwingt eine gültige Eingabe. Gültig sind 1 für menschlichen Spieler und 2 für Computergegner
            self.__gameMode = gameMode
        else:
            print("Wähle einen gültigen Spielmodus. 1 = Mensch, 2 = Computer")

    def __repr__(self):
        return f"Name: {self.__name}, Spielstein-ID: {self.__playerid}, Modus: {self.__gameMode}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def playerid(self):
        return self.__playerid

    @playerid.setter
    def playerid(self, value: str):
        self.__playerid = value

    @property
    def gameMode(self):
        return self.__gameMode

    def playDraw(self, gui: GUI) -> int:
        pass

class RuleSet:
    def __init__(self):
        pass

    def checkDraw(self, field: Field, col: int) -> bool:
        pass

    def checkPlayer(self, field: Field, player: Player) -> bool:
        pass

    def checkGameOver(self, field: Field) -> bool:
        pass


class FourWinsGame:
    def __init__(self,player1: Player, player2: Player):
        self.__player1 = player1
        self.__player2 = player2

    def initializeGame(self):
        pass

    def startGame(self):
        pass










if __name__ == '__main__':
    Player1 = Player("test", "x", 1)
    print(Player1)
