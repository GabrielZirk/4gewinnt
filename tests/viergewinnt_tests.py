import unittest
from game.viergewinnt import Player
from game.viergewinnt import Field
from game.viergewinnt import GUI
from game.viergewinnt import RuleSet

class ViergewinntTests(unittest.TestCase):

    def setUp(self):
        self.Player1 = Player("Player1", "X", 1)
        self.Player2 = Player("Player2", "O", 2)
        self.Feld1 = Field()
        self.gui1 = GUI()
        self.ruleset1 = RuleSet()

    ###################################################################
    # Tests der Klasse Player
    ###################################################################
    def test_incorrect_gameMode_input(self):
        """
        Überprüft, ob andere gameModi als "1" und "2" möglich sind.

        Returns
        -------
        Testresultate
        """
        self.assertRaises(ValueError, Player, "Invalid Game Mode3", "X", 3)
        self.assertRaises(ValueError, Player, "Invalid Game Mode0", "X", 0)

    ###################################################################
    # Tests der Klasse Field
    ###################################################################
    def test_setField(self):
        """
        Überprüft, ob die Spielsteine korrekt gesetzt werden.
        Returns
        -------
        Testergebnis
        """
        self.Feld1.setFields(0, "X")
        erg1 = self.Feld1.getFields()
        self.assertEqual(erg1, [[" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "],
                         ["X", " ", " ", " ", " ", " ", " "]])
        self.Feld1.setFields(0, "X")
        erg2 = self.Feld1.getFields()
        self.assertEqual(erg2, [[" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])
        self.Feld1.setFields(0, "O")
        self.Feld1.setFields(0, "O")
        self.Feld1.setFields(0, "O")
        erg3 = self.Feld1.getFields()
        self.assertEqual(erg3, [[" ", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])
        self.Feld1.setFields(0, "O")
        erg4 = self.Feld1.getFields()
        self.assertEqual(erg4, [["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])

    def test_valid_col(self):
        """
        Überprüft, ob ein ValueError angezeigt wird, wenn nicht 0, 2, 3, 4, 5, 6, oder 7 als Spaltenwert übergeben werden.
        Returns
        -------
        Testergebnis

        """
        self.assertRaises(ValueError, self.Feld1.setFields, 7, "X")
        self.assertRaises(TypeError, self.Feld1.setFields, "1", "X")

    ###################################################################
    # Tests der Klasse GUI
    ###################################################################
    def test_valid_gameMode(self):
        self.assertEqual(str, type(self.gui1.getName(1)))

    def test_gameMode(self):
        self.assertEqual(int, type(self.gui1.getGameMode("testuser")))

    def test_getLastRow(self):
        self.Feld1.setFields(1, "X")
        self.assertEqual(self.Feld1.getLastRow(), 5)
        self.Feld1.setFields(1, "O")
        self.assertEqual(self.Feld1.getLastRow(), 4)

    ###################################################################
    # Tests der Klasse RuleSet
    ###################################################################
    def test_checkDraw_pos(self):
        """
        Überprüft, ob ein Zug möglich ist.

        Ein Zug ist nicht möglich, wenn die Reihe schon voll ist.
        Returns
        -------
        Testergebnis
        """
        self.Feld1.setFields(1, "X")
        #self.gui1.outputField(self.Feld1)
        self.assertTrue(self.ruleset1.checkDraw(self.Feld1, 1))
        self.Feld1.setFields(1, "X")
        self.assertTrue(self.ruleset1.checkDraw(self.Feld1, 1))
        self.Feld1.setFields(1, "X")
        self.assertTrue(self.ruleset1.checkDraw(self.Feld1, 1))
        self.Feld1.setFields(1, "X")
        self.assertTrue(self.ruleset1.checkDraw(self.Feld1, 1))
        self.Feld1.setFields(1, "X")
        self.assertTrue(self.ruleset1.checkDraw(self.Feld1, 1))
        self.Feld1.setFields(1, "X")
        # self.gui1.outputField(self.Feld1)

    def test_checkDraw_neg(self):
        """
        Überprüft, ob ein Zug nicht möglich ist, weil Reihe schon voll ist.

        Ein Zug ist nicht möglich, wenn die Reihe schon voll ist.
        Returns
        -------
        Testergebnis
        """
        for _ in range(1, 6):
            self.Feld1.setFields(0, "X")
        # self.gui1.outputField(self.Feld1)
        self.Feld1.setFields(0, "X")
        # self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkDraw(self.Feld1, 0))

    def test_checkGameOver(self):
        """
        Überprüft, ob noch freie Felder auf dem Spielfeld sind.

        Befinden sich noch leere Felder auf dem Spielfeld wird False übergeben, ist das Spielfeld voll True.

        Returns
        -------
        Testergebnis
        """
        #self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkGameOver(self.Feld1))
        for _ in self.Feld1.getFields():
            for i in range(0, 7):
                self.Feld1.setFields(i, "X")
        #self.gui1.outputField(self.Feld1)
        self.assertTrue(self.ruleset1.checkGameOver(self.Feld1))

    def test_checkPlayerWon_row1(self):
        """
        Überprüft, ob bei 4 aufeinander folgenden Steinen in einer Reihe True ausgegeben wird.
        Returns
        -------
        Testergebnis

        """
        #self.gui1.outputField(self.Feld1)
        self.Feld1.setFields(1, "X")
        #self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(2, "X")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(3, "X")
        #self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(4, "X")
        self.assertTrue(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        #self.gui1.outputField(self.Feld1)

    def test_checkPlayerWon_row2(self):
        """
        Überprüft, ob bei 4 aufeinander folgenden Steinen in einer Reihe True ausgegeben wird.
        Returns
        -------
        Testergebnis

        """
        #self.gui1.outputField(self.Feld1)
        self.Feld1.setFields(1, "X")
        #self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(2, "O")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(3, "X")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(4, "X")
        #self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(5, "X")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(6, "X")
        self.assertTrue(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        #self.gui1.outputField(self.Feld1)

    def test_checkPlayerWon_col1(self):
        """
        Überprüft, ob bei 4 aufeinander folgenden gleichen Steinen in einer Spalte True ausgegeben wird.

        Returns
        -------
        Testergebnis
        """
        self.Feld1.setFields(0, "X")
        # self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(0, "O")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(0, "X")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(0, "X")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(0, "X")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        self.Feld1.setFields(0, "X")
        self.assertTrue(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))
        # self.gui1.outputField(self.Feld1)

    def test_checkPlayerWon_diag_linksoben_nach_rechtsunten_neg1(self):
        """
        Überprüft, ob in einer Diagonale (links oben nach rechts unten) nicht 4 gleiche Steine liegen.

        Returns
        -------
        Testergebnis
        """
        self.Feld1.setFields(1, "X")
        self.Feld1.setFields(1, "X")
        self.Feld1.setFields(1, "X")
        self.Feld1.setFields(2, "X")
        self.Feld1.setFields(1, "O")
        self.Feld1.setFields(3, "O")
        self.Feld1.setFields(3, "O")
        self.Feld1.setFields(2, "O")
        self.Feld1.setFields(2, "O")
        #self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player2))

    def test_checkPlayerWon_diag_linksoben_nach_rechtsunten_pos1(self):
        """
        Überprüft, ob in einer Diagonale (links oben nach rechts unten) 4 gleiche Steine liegen (positives Ergebnis).

        Returns
        -------
        Testergebnis
        """
        self.Feld1.setFields(1, "X")
        self.Feld1.setFields(1, "X")
        self.Feld1.setFields(1, "X")
        self.Feld1.setFields(2, "X")
        self.Feld1.setFields(1, "O")
        self.Feld1.setFields(3, "O")
        self.Feld1.setFields(3, "O")
        self.Feld1.setFields(2, "O")
        self.Feld1.setFields(2, "O")
        #self.gui1.outputField(self.Feld1)
        self.Feld1.setFields(4, "O")
        #self.gui1.outputField(self.Feld1)
        self.assertTrue(self.ruleset1.checkPlayerWon(self.Feld1, self.Player2))
        #self.gui1.outputField(self.Feld1)

    def test_checkPlayerWon_diag_linksoben_nach_rechtsunten_neg2(self):
        """
        Überprüft, ob in einer Diagonale (links oben nach rechts unten) nicht 4 gleiche Steine liegen.

        Returns
        -------
        Testergebnis
        """
        self.Feld1.setFields(6, "X")
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))

    def test_checkPlayerWon_diag_linksoben_nach_rechtsunten_pos2(self):
        """
        Überprüft, ob in einer Diagonale (links oben nach rechts unten) 4 gleiche Steine liegen.
        Returns
        -------
        Testergebnis
        """
        for _ in range(1, 4):
            for i in range(0, 7):
                self.Feld1.setFields(i, "X")
        self.Feld1.setFields(4, "X")
        # self.gui1.outputField(self.Feld1)
        self.assertTrue(self.ruleset1.checkPlayerWon(self.Feld1, self.Player1))

    def test_checkPlayerWon_diag_rechtsoben_nach_linksunten_neg1(self):
        """
        Überprüft, ob in einer Diagonale (rechts oben nach links unten) nicht 4 gleiche Steine liegen (negatives Ergebnis).
        Returns
        -------
        Testergebnis
        """
        for _ in range(1, 4):
            self.Feld1.setFields(4, "O")
        for _ in range(1, 3):
            self.Feld1.setFields(3, "O")
        self.Feld1.setFields(2, "O")
        # self.gui1.outputField(self.Feld1)
        self.assertFalse(self.ruleset1.checkPlayerWon(self.Feld1, self.Player2))

    def test_checkPlayerWon_diag_rechtsoben_nach_linksunten_pos1(self):
        """
        Überprüft, ob in einer Diagonale (rechts oben nach links unten) 4 gleiche Steine liegen (positives Ergebnis).
        Returns
        -------
        Testergebnis
        """
        for _ in range(1, 5):
            self.Feld1.setFields(5, "O")
        for _ in range(1, 4):
            self.Feld1.setFields(4, "O")
        for _ in range(1, 3):
            self.Feld1.setFields(3, "O")
        self.Feld1.setFields(2, "O")
        # self.gui1.outputField(self.Feld1)
        self.assertTrue(self.ruleset1.checkPlayerWon(self.Feld1, self.Player2))

    def test_checkPlayerWon_diag_rechtsoben_nach_linksunten_pos2(self):
        """
        Überprüft, ob in einer Diagonale (rechts oben nach links unten) 4 gleiche Steine liegen (positives Ergebnis).
        Returns
        -------
        Testergebnis
        """
        self.Feld1.setFields(2, "O")
        for _ in range(1, 4):
            self.Feld1.setFields(4, "O")
        for _ in range(1, 3):
            self.Feld1.setFields(3, "O")
        for _ in range(1, 5):
            self.Feld1.setFields(5, "O")
        # self.gui1.outputField(self.Feld1)
        self.assertTrue(self.ruleset1.checkPlayerWon(self.Feld1, self.Player2))

if __name__ == '__main__':
    unittest.main()