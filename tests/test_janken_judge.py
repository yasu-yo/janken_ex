import unittest
from source.janken_judge import judge

class TestJankenJudge(unittest.TestCase):
    def test_judge(self):
        # テストパターン: (computer_hand, player_hand, expected_result)
        test_cases = [
            ('グー', 'グー', 'draw'),
            ('グー', 'チョキ', 'computer_win'),
            ('グー', 'パー', 'player_win'),
            ('チョキ', 'グー', 'player_win'),
            ('チョキ', 'チョキ', 'draw'),
            ('チョキ', 'パー', 'computer_win'),
            ('パー', 'グー', 'computer_win'),
            ('パー', 'チョキ', 'player_win'),
            ('パー', 'パー', 'draw'),
        ]

        for computer_hand, player_hand, expected in test_cases:
            with self.subTest(computer_hand=computer_hand, player_hand=player_hand):
                self.assertEqual(judge(computer_hand, player_hand), expected)

if __name__ == '__main__':
    unittest.main()
