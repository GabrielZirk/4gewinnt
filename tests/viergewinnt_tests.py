import unittest
from game.viergewinnt import Player
from game.viergewinnt import Field


class PlayerTest(unittest.TestCase):

    def test_incorrect_gameMode_input(self):
        """
        Überprüft, ob andere gameModi als "1" und "2" möglich sind.

        Returns
        -------
        Testresultate
        """
        self.assertRaises(ValueError, Player, "Invalid Game Mode3", "X", 3)
        self.assertRaises(ValueError, Player, "Invalid Game Mode0", "X", 0)

    def setUp(self) -> None:
        self.Player1 = Player("Player1", "X", 1)
        self.Player2 = Player("Player2", "O", 2)


class FieldsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Feld1 = Field()

    def test_setField(self):
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
        self.Feld1.setFields(0, "O")
        erg5 = self.Feld1.getFields()
        self.assertEqual(erg5, [["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])


if __name__ == '__main__':
    unittest.main()