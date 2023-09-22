import unittest
from unittest.mock import patch
from io import StringIO
import random
from datetime import date
from Lucky_number import LuckyNumberGame

# Define a test class for LuckyNumberGame
class TestLuckyNumberGame(unittest.TestCase):

    # Test case: Testing the get_player_name() method
    @patch('builtins.input', side_effect=['Susan'])
    def test_get_player_name(self, mock_input):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Simulate user input with the name 'Susan'
        game.get_player_name()
        # Check if the player_name attribute was correctly set
        self.assertEqual(game.player_name, 'Susan')

    # Test case: Testing the get_player_birthdate() method
    @patch('builtins.input', side_effect=['19770712'])
    def test_get_player_birthdate(self, mock_input):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Simulate user input with the birthdate '19770712'
        game.get_player_birthdate()
        # Check if the player_birthdate attribute was correctly set
        self.assertEqual(game.player_birthdate, '19770712')

    # Test case: Testing the calculate_player_age() method
    def test_calculate_player_age(self):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Set the player_birthdate attribute to '19770712'
        game.player_birthdate = '19770712'
        # Calculate the player's age based on the birthdate
        game.calculate_player_age()
        # Check if the player_age attribute was correctly calculated
        self.assertEqual(game.player_age, 46)

    # Test case: Testing the generate_lucky_list() method
    @patch('random.sample', return_value=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_generate_lucky_list(self, mock_sample):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Generate a list of lucky numbers
        game.generate_lucky_list()
        # Check if the lucky_list attribute was correctly generated
        self.assertEqual(game.lucky_list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Test case: Testing the generate_lucky_number() method
    @patch('random.randint', return_value=42)
    def test_generate_lucky_number(self, mock_randint):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Generate a lucky number
        game.generate_lucky_number()
        # Check if the lucky_number attribute was correctly generated
        self.assertEqual(game.lucky_number, 42)
        # Check if the generated lucky number is added to the lucky_list
        self.assertEqual(game.lucky_list, [42])

    # Test case: Testing the play_game() method for correct guess
    @patch('builtins.input', side_effect=['42', 'n'])
    def test_play_game_correct_guess(self, mock_input):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Set the lucky_number and lucky_list attributes
        game.lucky_number = 42
        game.lucky_list = [42]
        # Simulate user input for a correct guess
        with patch('builtins.print') as mock_print:
            game.play_game()
            # Check if the correct message is printed
            mock_print.assert_called_with("Congratulations! You got the lucky number from try #1")

    # Test case: Testing the play_game() method for incorrect guesses
    @patch('builtins.input', side_effect=['50', '51', '52', '42', 'n'])
    def test_play_game_incorrect_guess(self, mock_input):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Set the lucky_number and lucky_list attributes
        game.lucky_number = 42
        game.lucky_list = [42]
        # Simulate user input for incorrect guesses
        with patch('builtins.print') as mock_print:
            game.play_game()
        # Check if the tries_count is incremented correctly
        self.assertEqual(game.tries_count, 4)
        # Check if the message with the correct try number is printed
        self.assertIn("This is try #1, and the new list is:", mock_print.call_args_list[0][0][0])

    # Test case: Testing the play_game() method for invalid inputs
    @patch('builtins.input', side_effect=['abc', '50', '51', '52', '42', 'n'])
    def test_play_game_invalid_input(self, mock_input):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Set the lucky_number and lucky_list attributes
        game.lucky_number = 42
        game.lucky_list = [42]
        # Simulate user input for invalid inputs
        with patch('builtins.print') as mock_print:
            game.play_game()

    # Test case: Testing the reset_game() method
    @patch('builtins.input', side_effect=['n'])
    def test_reset_game(self, mock_input):
        # Create an instance of LuckyNumberGame
        game = LuckyNumberGame()
        # Set some initial values for game attributes
        game.player_name = 'Susan'
        # Reset the game
        game.reset_game()
        # Check if all game attributes are reset to their initial values
        self.assertIsNone(game.player_name)
        self.assertIsNone(game.player_birthdate)
        self.assertIsNone(game.player_age)
        self.assertEqual(game.lucky_list, [])
        self.assertIsNone(game.lucky_number)
        self.assertEqual(game.tries_count, 0)

#  running the unit tests
if __name__ == '__main__':
    unittest.main()


