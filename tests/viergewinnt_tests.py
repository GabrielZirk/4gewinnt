import unittest
from game.viergewinnt import Player

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

    def SetUp(self) -> None:
        self.Player1 = Player("Player1", "X", 1)
        self.Player2 = Player("Player2", "O", 2)



if __name__ == '__main__':
    unittest.main()