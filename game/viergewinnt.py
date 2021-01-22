from typing import List
from random import randint

class Field:
    """
    In der Feld-Klasse befinden sich alle aktuellen Informationen zu dem Spielfeld.

    Das Spielfeld wurde als Array (eine Liste aus Listen) umgesetzt. Die 6 Listen bestehen jeweils aus 7 str.
    """
    def __init__(self):
        self.__fields = [[" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "]]

    def getFields(self) -> List:
        return self.__fields

    def setFields(self, col: int, playerid: str):
        """
        Setzt einen Spielstein in eine Spalte.

        Es wird bei jedem Spielzug darauf geachtet, dass der Spielstein nicht in der Luft schwebt und immer bis zum niedrigst-möglichen Punkt herunterfällt.
        Parameters
        ----------
        col: int
            Gibt die Spalte an, in die der Spielstein geworfen wird.

        playerid: str
            Gibt an welcher Spielstein geworfen wird.

        Returns
        -------
        Nichts.
        """
        reihe = 0
        geworfen = False
        for list in reversed(self.__fields):
            if geworfen == False:
                if list[col] == " ":
                    list[col] = str(playerid) #Stellt zusätzlich sicher, dass auch ein str eingetragen wird.
                    reihe += 1
                    geworfen = True
                elif list[col] != " ":
                    reihe += 1


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
        if gameMode == 1 or gameMode == 2: # Erzwingt eine gültige Eingabe. Gültig sind 1 für menschlichen Spieler und 2 für Computergegner.
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

        Die Methode überprüft zuerst, ob der Spieler ein Mensch (gameMode = 1) oder ein Computer (gameMode = 2) ist.
        Ist der Spieler ein Mensch, wird die gewählte Spalte übernommen.
        Ist der Spieler ein Computer wird zufällig eine Spalte gewählt

        Parameters
        ----------
        gui: GUI
        Übergibt den Namen des GUI (graphical user interface) um dort die Methode `getDraw()`aufzurufen, wenn der Spieler ein Mensch ist.

        Returns
        -------
        `col`
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
    pass
    # field = [[" ", " ", " ", " ", " ", " ", " "],
    #                      [" ", " ", " ", " ", " ", " ", " "],
    #                      [" ", " ", " ", " ", " ", " ", " "],
    #                      [" ", " ", " ", " ", " ", " ", " "],
    #                      [" ", " ", " ", " ", " ", " ", " "],
    #                      [" ", " ", " ", " ", " ", " ", " "]]
    # # print(len(field))
    # # x = list(range(len(field)-1, -1, -1))
    # # print(x)
    #
    #
    # def ausgabe(field):
    #     for list in field:
    #         print(list)
    #
    # ausgabe(field)
    # def setdraw(col, playerid):
    #     reihe = 0
    #     geworfen = False
    #     for list in reversed(field):
    #         if geworfen == False:
    #             if list[col] == " ":
    #                 list[col] = str(playerid)
    #                 reihe += 1
    #                 print(reihe)
    #                 geworfen = True
    #             elif list[col] != " ":
    #                 reihe += 1
    #
    #
    # setdraw(0, "X")
    # ausgabe(field)
    # setdraw(0, "X")
    # ausgabe(field)
    # setdraw(0, "X")
    # ausgabe(field)
    # setdraw(1, "X")
    # ausgabe(field)
    # feld = Field()
    # print(feld)
    # print(feld.getFields())
    # feld.setFields(1, "X")
    # print(feld.getFields())