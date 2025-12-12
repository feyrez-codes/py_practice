from utils import Player_Resources, coin_flip
import unittest
from unittest.mock import patch, call
from datetime import datetime


class TestUtils(unittest.TestCase):

  @patch('utils.input')
  def test_greeting(self, mock_input):
    #set up testable instances
    player = Player_Resources()
    cpu = Player_Resources(0,"tic-tac-toby")
    mock_input.side_effect = ["Cole_Test", "$"]

    result = Player_Resources.greeting(player, cpu)

    with patch("utils.datetime") as mock_datetime:
      #test morning response:
      mock_datetime.now.return_value = datetime(2025, 11, 17, 11, 30, 0)

      #test afternoon response:
      mock_datetime.now.return_value = datetime(2025, 11, 17, 12, 0, 0)
      self.assertEqual(result, player.fname)
      input.assert_called_with("Good afternoon, challenger! What should I call you? ")

      #test evening response:
      mock_datetime.now.return_value = datetime(2025, 11, 17, 18, 0, 0)
      self.assertEqual(result, player.fname)
      input.assert_called_with("Good evening, challenger! What should I call you? ")

      #test night response:
      mock_datetime.now.return_value = datetime(2025, 11, 17, 18, 30, 0)
      self.assertEqual(result, player.fname)
      input.assert_called_with("Good night, challenger! What should I call you? ")

  @patch("builtins.input")
  def test_coin_flip(self, input):
    #test that names return correctly:
    name_test = 'Cole_Test'
    coin_flip(name_test)
    input.assert_called_with("Alright, Cole_Test, time to get down to business. Let's flip a coin to see who goes first. Please choose heads or tails? ")
    
    #test that results return correctly:


if __name__ == '__main__':
  unittest.main()