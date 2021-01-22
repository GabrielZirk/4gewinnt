from typing import List
from random import randint

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
    def outputField(self, field: Field):
        pass

    def getName(self, playerNr: int) -> str:
        pass

    def getGameMode(self, name: str) -> int:
        pass

    def getDraw(self, name: str):
        pass

class Player:
    """
    Aus der Klasse Player kann ein Objekt Spieler erstellt werden.

    Ein Spieler kann entweder ein Mensch oder ein Computer sein.
    Außerdem wird er durch seinen Namen und seinen Spielstein repräsentiert.

    Attributes
    ----------
    name : str
        Übernimmt den Namen des Spielers.
    playerid : str
        Legt den Spielstein bzw. das Symbol fest, welches den Spieler am Spielfeld repräsentiert.
    gameMode: int
        Legt fest, ob ein Spieler ein Mensch (Wert = 1) oder ein Computer (Wert = 2) ist. Andere Werte sind nicht zulässig. Die if-Schleife bei der Zuweisung von `gameMode` erzwingt eine gültige Eingabe.
    """
    def __init__(self, name: str, playerid: str,  gameMode: int):
        self.__name = name
        self.__playerid = playerid
        # Erzwingt eine gültige Eingabe. Gültig sind 1 für menschlichen Spieler und 2 für Computergegner.
        if gameMode == 1 or gameMode == 2:
            self.__gameMode = gameMode
        else:
            raise ValueError("Wähle einen gültigen Spielmodus. 1 = Mensch, 2 = Computer")

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
        """
        Führt den Spielzug aus.

        Die Methode überprüft zuerst, ob der Spieler ein Mensch oder ein Computer ist.
        Ist der Spieler ein Mensch, wird die gewählte Spalte übernommen.
        Ist der Spieler ein Computer wird zufällig eine Spalte gewählt

        Parameters
        ----------
        gui: GUI
        Übergibt den Namen des GUI (graphical user interface) um dort die Methode `getDraw()`aufzurufen, wenn der Spieler ein Mensch ist.

        Returns
        -------
        Spalte `col`

        """
        if self.__gameMode == 1:
            col = gui.getDraw(self.__name)
            return col
        elif self.__gameMode == 2:
            col = randint(1, 8)
            print("Col: ", col)
            return col

class RuleSet:
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
    Player1 = Player("test", "x", 3)
    print(Player1)
