# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:20:36 2022

@author: riku.sjoroos
"""

import unittest
import sys

sys.path.append('..')

from helloworld import hello

class HelloTestcase(unittest.TestCase):
    def test_message_appeared(self):
        hello()
        succeed =input("Did the message appeared? (y/n)")
        succeed = succeed.lower()[0]
        self.assertEqual(succeed, 'y')
    
    def test_message_correct(self):
        hello()
        succeed =input("Is the message 'Hello World' (y/n)")
        succeed = succeed.lower()[0]
        self.assertEqual(succeed, 'y')

if __name__ == "__main__":
    unittest.main()


