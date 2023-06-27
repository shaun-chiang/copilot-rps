# Write tests for rock, paper, scissors game
# 1. Player vs Computer
# 2. First to 3 wins
# 3. Write tests for:
#     1. Invalid choice
#     2. Tie
#     3. Player win
#     4. Computer win

import unittest
from src.rps import rock_paper_scissors

class TestRockPaperScissors(unittest.TestCase):
    def test_player_win(self):
        self.assertEqual(rock_paper_scissors("rock", "scissors"), "You win!")
        self.assertEqual(rock_paper_scissors("paper", "rock"), "You win!")
        self.assertEqual(rock_paper_scissors("scissors", "paper"), "You win!")

    def test_computer_win(self):
        self.assertEqual(rock_paper_scissors("rock", "paper"), "You lose!")
        self.assertEqual(rock_paper_scissors("paper", "scissors"), "You lose!")
        self.assertEqual(rock_paper_scissors("scissors", "rock"), "You lose!")

    def test_invalid_choice(self):
        self.assertEqual(rock_paper_scissors("rock", "r"), "Invalid choice!")
        self.assertEqual(rock_paper_scissors("p", "paper"), "Invalid choice!")
        self.assertEqual(rock_paper_scissors("scissors", "s"), "Invalid choice!")

    def test_tie(self):
        self.assertEqual(rock_paper_scissors("rock", "rock"), "Tie!")
        self.assertEqual(rock_paper_scissors("paper", "paper"), "Tie!")
        self.assertEqual(rock_paper_scissors("scissors", "scissors"), "Tie!")

if __name__ == '__main__':
    unittest.main()