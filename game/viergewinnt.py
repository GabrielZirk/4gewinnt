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

    def setFields(self, col: int, playerid: str): #alles in eine while true schleife packen, damit der spielzug so lange wiederholt wird bis ein korrekter wert eingegeben wurde?
        """
        Setzt einen Spielstein in eine Spalte.

        Mögliche Spalten sind 1-7 (nur int). Es wird bei jedem Spielzug darauf geachtet, dass der Spielstein nicht in der Luft schwebt und immer bis zum niedrigst-möglichen Punkt herunterfällt.
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
        if type(col) != int: #Stellt sicher, dass nur ganze Zahlen übergeben werden.
            raise TypeError("Nur ganze Zahlen von 1 bis 7 sind erlaubt.")

        valid_cols = [1, 2, 3, 4, 5, 6, 7]
        if col not in valid_cols: #Stellt sicher, dass nur ganze Zahlen von 1 bis 7 übergeben werden können.
            raise ValueError("Wähle eine gültige Spalte (1 - 7).")


        reihe = 0
        geworfen = False
        for list in reversed(self.__fields):
            if geworfen == False:
                if list[col-1] == " ":
                    list[col-1] = str(playerid) #Stellt  sicher, dass auch ein str eingetragen wird.
                    reihe += 1
                    geworfen = True
                elif list[col-1] != " ":
                    reihe += 1


    def getLastRow(self, col: int, row: int) -> int:
        pass

    def getLastCol(self) -> int:
        pass

class GUI:
    def outputField(self, field: Field):
        """Gibt das Spielfeld aus"""
        for list in field.getFields():
            print(" | ", list[0], " | ", list[1], " | ", list[2], " | ", list[3], " | ", list[4], " | ", list[5], " | ",
                  list[6], " | ")
            print(" |-----------------------------------------|")

    def getName(self, spielernr: int) -> str:
        """
        Fordert die Spieler auf ihre Namen einzugeben.
        Parameters
        ----------
        spielernr: int

        Returns
        -------
        Name des Spielers
        """
        name = input(f"Name des Spielers {spielernr}: ")
        return name

    def getGameMode(self, name: str) -> int:
        """
        Die Methode fordert beim Spieler die Eingabe des Spielmodus an.

        Die Aufforderung wird so lange wiederholt, bis eine gültige Eingabe (1 = Mensch, 2 = Computer) erfolgt ist.
        Parameters
        ----------
        name: str
            Der Name des Spielers würd übergeben, damit er angesprochen werden kann.

        Returns
        -------
        Spielmodus
        """
        valid_modes = [1, 2]
        spielmodus = 0
        while spielmodus not in valid_modes:
            try:
                spielmodus = int(input(f'{name.capitalize()} bist du ein Mensch (wähle "1") oder ein Computer (wähle "2"): '))
                if spielmodus not in valid_modes:
                    print('Achtung: Wähle "1" für Mensch und "2" für Computer!')
            except ValueError:
                print('Achtung: Wähle "1" für Mensch und "2" für Computer!')
        return int(spielmodus)

    def getDraw(self, name: str):
        spalte = 0
        valid_cols = [1, 2, 3, 4, 5, 6, 7]
        while spalte not in valid_cols:
            try:
                spalte = int(input(f'{name.capitalize()} in welche Spalte möchtest du werfen? '))
                if spalte not in valid_cols:
                    print("Achtung: Wähle eine Spalte von 1 bis 7!")
            except ValueError:
                print("Achtung: Wähle eine Spalte von 1 bis 7!")
        return spalte - 1

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
        Übergibt den Namen des GUI (graphical user interface), um dort die Methode `getDraw()`aufzurufen, wenn der Spieler ein Mensch ist.

        Returns
        -------
        `spalte`
        """
        if self.__gameMode == 1:
            spalte = gui.getDraw(self.__name)
            return spalte
        elif self.__gameMode == 2:
            spalte = randint(1, 8)
            print("Spalte: ", spalte)
            return spalte

class RuleSet:
    def checkDraw(self, field: Field, col: int) -> bool:
        """
        Überprüft, ob ein Spielzug möglich ist.

        Ein Spielzug ist nicht möglich, wenn die letzte Reihe der gewählten Spalte schon mit einem Spielstein belegt ist.

        Parameters
        ----------
        field: Field
            Übergibt das Spielfeld.
        col: int
            Übergibt die Spalte in die geworfen werden soll.

        Returns
        -------
        True oder False

        """
        spielfeld = field.getFields()
        if spielfeld[0][col] != " ":
            return False
        else:
            return True

    def checkPlayerWon(self, field: Field, player: Player) -> bool:
        pass

    def checkGameOver(self, field: Field) -> bool:
        """
        Überprüft, ob das Spielfeld voll ist.

        Solange noch freie Felder am Spielfeld sind, wird False geliefert. Ist das Spielfeld voll wird True geliefert.
        Parameters
        ----------
        field: Field
            Das übergebene Spielfeld wird überprüft.

        Returns
        -------
        True oder False.

        """
        counter_befuellte_felder = 0
        spielfeld = field.getFields()
        for list in spielfeld:
            for item in list:
                if item != " ":
                    counter_befuellte_felder += 1
        print(counter_befuellte_felder)
        if counter_befuellte_felder < 42:
            return False
        else:
            return True

class FourWinsGame:
    def __init__(self,player1: Player, player2: Player):
        self.__player1 = player1
        self.__player2 = player2

    def initializeGame(self):
        pass

    def startGame(self):
        pass



if __name__ == '__main__':
    feld1 = Field()
    gui1 = GUI()
    ruleset1 = RuleSet()
    gui1.outputField(feld1)
    print(ruleset1.checkGameOver(feld1))
    for list in feld1.getFields():
        for i in range(1, 8):
            print(i)
            feld1.setFields(i, "X")
    gui1.outputField(feld1)
    print(ruleset1.checkGameOver(feld1))




