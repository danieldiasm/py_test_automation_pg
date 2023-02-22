# File: test_app.py
# Author: Daniel Z. Dias de Moraes
# Last update: 22 Feb 2023
#
# The tests on this file should be Unit Tests, although the second test
# can be considered an integration test, because "add_one" make use of 
# "app.ordenate list" internally to get its job done.
#
# Basically that is the erro done in purpose mentioned on the Readme.
# The soultion is on the test_mock.py file
from unittest import TestCase

import application.app as app

class TestApp(TestCase):

    def test_ordenate_list(self):

        source_list = [2,0,5,3,1,4,6]
        expected_result = [0,1,2,3,4,5,6]

        result_list = app.ordenate_list(source_list)

        self.assertListEqual(expected_result, result_list)
    

    def test_add_one(self):

        source_list = [2,0,5,3,1,4,6]
        expected_result = [0,1,2,3,4,5,6,7]

        result_list = app.add_one(source_list)

        self.assertListEqual(expected_result, result_list)
