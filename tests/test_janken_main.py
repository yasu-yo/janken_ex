import sys
import unittest
from unittest.mock import patch

# sourceディレクトリをシステムパスに追加
sys.path.append('./source')

from source.janken_main import main

class TestMain(unittest.TestCase):
    
    @patch('player.player_pon', return_value='チョキ')
    @patch('computer.computer_pon', return_value='グー')
    def test_computer_win(self, mock_computer_pon, mock_player_pon):
        with patch('builtins.print') as mock_print:
            main()
        self.assertEqual(mock_computer_pon.call_count, 3)
        self.assertEqual(mock_player_pon.call_count, 3)
        
    @patch('player.player_pon', return_value='パー')
    @patch('computer.computer_pon', return_value='グー')
    def test_player_win(self, mock_computer_pon, mock_player_pon):
        with patch('builtins.print') as mock_print:
            main()
        self.assertEqual(mock_computer_pon.call_count, 3)
        self.assertEqual(mock_player_pon.call_count, 3)

if __name__ == '__main__':
    unittest.main()