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
        self.__letzte_bespielte_spalte = None
        self.__letzte_bespielte_reihe = None
    #     self.__last_player = None Nicht sicher, ob ich die brauchen werde
    #
    # def getLastPlayer(self):
    #     return self.__last_player

    def getFields(self) -> List:
        """
        Übergibt das Spielfeld

        Returns
        -------
        List [List] - self.__fields
        """
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
        self.__letzte_bespielte_spalte = col
        if type(col) != int: #Stellt sicher, dass nur ganze Zahlen übergeben werden.
            raise TypeError("Nur ganze Zahlen von 1 bis 7 sind erlaubt.")

        valid_cols = [0, 1, 2, 3, 4, 5, 6]
        if col not in valid_cols: #Stellt sicher, dass nur ganze Zahlen von 1 bis 7 übergeben werden können.
            raise ValueError("Wähle eine gültige Spalte (1 - 7).")


        reihe = 5
        geworfen = False
        for list in reversed(self.__fields):
            if geworfen == False:
                if list[col] == " ":
                    list[col] = str(playerid) #Stellt  sicher, dass auch ein str eingetragen wird.
                    #print(reihe)
                    #reihe += 1
                    self.__letzte_bespielte_reihe = reihe
                    geworfen = True
                elif list[col] != " ":
                    reihe -= 1
                    self.__letzte_bespielte_reihe = reihe


    def getLastRow(self) -> int:
        """
        Gibt die letzte bespielte Reihe aus.

        Die Reihenzählung beginnt von oben mit 0 und geht nach unten bis 5 (python Zählweise).

        Returns
        -------
        int, Reihennummer

        """
        return self.__letzte_bespielte_reihe

    def getLastCol(self) -> int:
        """
        Gibt die letzte bespielte Spalte aus.

        Die Spaltenzählung beginng von links mit 0 (Python Indexierung).

        Returns
        -------
        int, Spaltennummer
        """
        return self.__letzte_bespielte_spalte

class GUI:
    """
    Erzeugt das graphical user interface.
    """

    def outputField(self, field: Field):
        """Gibt das Spielfeld aus"""
        for list in field.getFields():
            print(" | ", list[0], " | ", list[1], " | ", list[2], " | ", list[3], " | ", list[4], " | ", list[5], " | ",
                  list[6], " | ")
            print(" |-----------------------------------------|")
        print(" |  1  |  2  |  3  |  4  |  5  |  6  |  7  | ")

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
                spielmodus = int(input(f'{name.capitalize()} bist du ein Mensch (wähle "1") oder ein Computer (wähle "2")?: '))
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
                continue
                # print("Achtung: Wähle eine Spalte von 1 bis 7!")
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

    @gameMode.setter
    def gameMode(self, value):
        self.__gameMode = value

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
            spalte = randint(0, 6)
            print("Computer spielt Spalte: ", spalte + 1)
            return spalte

class RuleSet:
    """
    Erzeugt das Regelwerk des Spiels 4gewinnt.
    """

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
        # print(spielfeld[0][col])
        if spielfeld[0][col] != " ":
            print("Spielzug nicht möglich. Spalte voll.")
            return False
        else:
            return True

    def checkPlayerWon(self, field: Field, player: Player) -> bool:
        last_set_row = field.getLastRow()
        # print("letzte gesetzte reihe: ",last_set_row)
        last_set_col = field.getLastCol()
        # print("letzte gesetzte spalte :", last_set_col)
        spielfeld = field.getFields()
        player_id = player.playerid

        #Überprüft die Reihen nach 4 aufeinanderfolgenden Spielsteinen des Spielers
        counter_reihe = 0
        for pos_reihe in range(0, 7):
            # print(spielfeld[0][0])
            if spielfeld[last_set_row][pos_reihe] == player_id:
                counter_reihe += 1
                if counter_reihe == 4:
                    return True
            elif spielfeld[last_set_row][pos_reihe] != player_id:
                counter_reihe = 0
                #print(counter_reihe)


        # Überprüft die Spalten nach 4 aufeinanderfolgenden Spielsteinen des Spielers
        counter_spalte = 0
        for pos_spalte in range(0, 6):
            if spielfeld[pos_spalte][last_set_col] == player_id:
                counter_spalte += 1
                if counter_spalte == 4:
                    return True
            else:
                counter_spalte = 0

        # Überprüft die Diagonale von links oben nach rechts unten nach gleichen Spielsteinen.
        counter_diagonale_linksoben_nach_rechtsunten = 0
        for i in range(-3, 4):
            if (last_set_col + i >= 0) and (last_set_col + i <= 6) and (last_set_row + i >= 0) and (last_set_row + i <= 5):
                try:
                    if spielfeld[last_set_row + i][last_set_col + i] == player_id:
                        counter_diagonale_linksoben_nach_rechtsunten += 1
                        # print("Check LoRu", spielfeld[last_set_row + i][last_set_col + i], i,
                        #     counter_diagonale_linksoben_nach_rechtsunten)
                        if counter_diagonale_linksoben_nach_rechtsunten == 4:
                            return True
                    elif spielfeld[last_set_row + i][last_set_col + i] != player_id:
                        counter_diagonale_linksoben_nach_rechtsunten = 0
                except IndexError:
                    counter_diagonale_linksoben_nach_rechtsunten = 0
                    # print("test_indexerror LoRu", last_set_row + i, last_set_col + i)
                    continue

        # Überprüft die Diagonale von links unten nach rechts oben nach gleichen Spielsteinen
        counter_diagonale_rechtsoben_nach_linksunten = 0
        for i in range(-3, 4):
            if (last_set_col + i >= 0) and (last_set_col + i <= 6) and (last_set_row - i >= 0) and (last_set_row - i <= 5):
                try:
                    if spielfeld[last_set_row - i][last_set_col + i] == player_id:
                        counter_diagonale_rechtsoben_nach_linksunten += 1
                        # print("Check LuRo", spielfeld[last_set_row - i][last_set_col + i], i,
                            # counter_diagonale_rechtsoben_nach_linksunten)
                        if counter_diagonale_rechtsoben_nach_linksunten == 4:
                            return True
                    elif spielfeld[last_set_row - i][last_set_col + i] != player_id:
                            counter_diagonale_rechtsoben_nach_linksunten = 0
                except IndexError:
                    counter_diagonale_rechtsoben_nach_linksunten = 0
                    # print("test_indexerror LuRo", last_set_row - i, last_set_col + i)
                    continue
        return False

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
        # print(counter_befuellte_felder)
        if counter_befuellte_felder < 42:
            return False
        else:
            return True

class FourWinsGame:
    """
    Erstellt das Spiel.
    """

    def __init__(self, player1id: str, player2id: str):
        self.__player1id = player1id
        self.__player2id = player2id
        self.__feld = Field()
        self.__gui = GUI()
        self.__ruleset = RuleSet()
        self.__player1 = Player("alias1", self.__player1id, 2)
        self.__player2 = Player("alias2", self.__player2id, 2)

    def initializeGame(self):
        """
        Fragt nach Name und gameMode der Spieler 1 und 2.

        Returns
        -------
        Nichts
        """
        name_player1 = self.__gui.getName(1)
        gamemode_player1 = self.__gui.getGameMode(name_player1)
        name_player2 = self.__gui.getName(2)
        gamemode_player2 = self.__gui.getGameMode(name_player2)
        self.__player1.name = name_player1
        self.__player1.gameMode = gamemode_player1
        self.__player2.name = name_player2
        self.__player2.gameMode = gamemode_player2
        self.__winner = None

    def startGame(self):
        """
        Diese Methode leitet durchs Spiel. Abwechselnd darf jeder Spieler seinen Spielstein werfen. Nach jedem Zug wird überprüft, ob das Spielfeld voll ist, bzw. ob ein Spieler gewonnen hat.
        Returns
        -------
        Nichts
        """
        self.__gui.outputField(self.__feld)
        while True:
            check_draw_player1 = False
            draw_player_1 = None
            while not check_draw_player1:
                draw_player_1 = self.__player1.playDraw(self.__gui)
                check_draw_player1 = self.__ruleset.checkDraw(self.__feld, draw_player_1)

            self.__feld.setFields(draw_player_1, self.__player1.playerid)
            self.__gui.outputField(self.__feld)
            if self.__ruleset.checkGameOver(self.__feld):
                print("Das Spielfeld ist voll. Das Spiel ist vorbei")
                break
            if self.__ruleset.checkPlayerWon(self.__feld, self.__player1):
                print(f"Herzlichen Glückwunsch {self.__player1.name}. Gut gespielt! :)")
                break

            check_draw_player2 = False
            draw_player_2 = None
            while not check_draw_player2:
                draw_player_2 = self.__player2.playDraw(self.__gui)
                #print(draw_player_2)
                check_draw_player2 = self.__ruleset.checkDraw(self.__feld, draw_player_2)

            self.__feld.setFields(draw_player_2, self.__player2.playerid)
            self.__gui.outputField(self.__feld)
            if self.__ruleset.checkGameOver(self.__feld):
                print("Das Spielfeld ist voll. Das Spiel ist vorbei")
                break
            if self.__ruleset.checkPlayerWon(self.__feld, self.__player2):
                print(f"Herzlichen Glückwunsch {self.__player2.name}. Gut gespielt! :)")
                break



if __name__ == '__main__':
    game = FourWinsGame("X", "O")
    game.initializeGame()
    game.startGame()