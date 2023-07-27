import unittest
from crackle_pop import CracklePop


class MyTestCase(unittest.TestCase):
    def test_1_to_100_display_correctly(self):
        actual = CracklePop.print()
        expected = ['1', '2', 'Crackle', '4', 'Pop', 'Crackle', '7', '8', 'Crackle', 'Pop', '11', 'Crackle', '13', '14',
                    'CracklePop', '16', '17', 'Crackle', '19', 'Pop', 'Crackle', '22', '23', 'Crackle', 'Pop', '26',
                    'Crackle', '28', '29', 'CracklePop', '31', '32', 'Crackle', '34', 'Pop', 'Crackle', '37', '38',
                    'Crackle', 'Pop', '41', 'Crackle', '43', '44', 'CracklePop', '46', '47', 'Crackle', '49', 'Pop',
                    'Crackle', '52', '53', 'Crackle', 'Pop', '56', 'Crackle', '58', '59', 'CracklePop', '61', '62',
                    'Crackle', '64', 'Pop', 'Crackle', '67', '68', 'Crackle', 'Pop', '71', 'Crackle', '73', '74',
                    'CracklePop', '76', '77', 'Crackle', '79', 'Pop', 'Crackle', '82', '83', 'Crackle', 'Pop', '86',
                    'Crackle', '88', '89', 'CracklePop', '91', '92', 'Crackle', '94', 'Pop', 'Crackle', '97', '98',
                    'Crackle', 'Pop']
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
