import unittest
from crackle_pop import CracklePop


class MyTestCase(unittest.TestCase):
    def test_1_to_100_display_correctly(self):
        actual = CracklePop.print()
        self.assertEqual(actual[0:15], ['1', '2', 'Crackle', '4', 'Pop', 'Crackle', '7', '8', 'Crackle', 'Pop',
                                        '11', 'Crackle', '13', '14', 'CracklePop'])
        self.assertEqual(actual[15:30], ['16', '17', 'Crackle', '19', 'Pop', 'Crackle', '22', '23', 'Crackle', 'Pop',
                                         '26', 'Crackle', '28', '29', 'CracklePop'])
        self.assertEqual(actual[30:45], ['31', '32', 'Crackle', '34', 'Pop', 'Crackle', '37', '38', 'Crackle', 'Pop',
                                         '41', 'Crackle', '43', '44', 'CracklePop'])
        self.assertEqual(actual[45:60], ['46', '47', 'Crackle', '49', 'Pop', 'Crackle', '52', '53', 'Crackle', 'Pop',
                                         '56', 'Crackle', '58', '59', 'CracklePop'])
        self.assertEqual(actual[60:75], ['61', '62', 'Crackle', '64', 'Pop', 'Crackle', '67', '68', 'Crackle', 'Pop',
                                         '71', 'Crackle', '73', '74', 'CracklePop'])
        self.assertEqual(actual[75:90], ['76', '77', 'Crackle', '79', 'Pop', 'Crackle', '82', '83', 'Crackle', 'Pop',
                                         '86', 'Crackle', '88', '89', 'CracklePop'])
        self.assertEqual(actual[90:100], ['91', '92', 'Crackle', '94', 'Pop', 'Crackle', '97', '98', 'Crackle', 'Pop'])


if __name__ == '__main__':
    unittest.main()
