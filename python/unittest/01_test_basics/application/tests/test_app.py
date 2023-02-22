# The tests on this file should be Unit Tests, although the second test
# might be considered an integration test, because "add_one" utilizes 
# "ordenate list" internally to get its job done.
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
