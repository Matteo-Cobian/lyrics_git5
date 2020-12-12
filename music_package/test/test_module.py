import unittest
import sys
import os
from music_package import lyrics as ly
import json

dictionary = {'Adele': 5}

class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(ly.get_lyric('Descendents', 'All'), 'All!')

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(ly.get_lyric(" "," "), "")
    
    #dictionary = {'Adele': 5}
    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(ly.get_lyric(1,1), "")

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(return_birthday([]), None)


        
        
if __name__ == "__main__":
    
    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=False)