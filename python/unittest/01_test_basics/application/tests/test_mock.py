# File: test_app.py
# Author: Daniel Z. Dias de Moraes
# Last update: 22 Feb 2023
#
# In order to isolate the "app.add_one" and "app.remove_one" to have this as 
# Unit Tests, the ideal is to do some sort of dependency injection, one way to
# do so is using "Mocking", and Mock the "app.ordenate_list" function.
#
# Pay attention to the import and construction:
#
# from unittest.mock import MagicMock
# app.ordenate_list = MagicMock()
#
# Mock will "simulate" the actions of app.ordenate_list, becoming possible
# to isolate the code of the "app.add_one" and testing it as a unit.

from unittest import TestCase
from unittest.mock import MagicMock

import application.app as app


class TestWithMock(TestCase):

        def test_mock_add_one(self):
            app.ordenate_list = MagicMock()
            app.ordenate_list.return_value = [0,1,2,3,4,5,6,7]

            source_list = [2,0,5,3,1,4,6]
            expected_result = [0,1,2,3,4,5,6,7,8]

            actual_result = app.add_one(source_list)

            self.assertListEqual(expected_result, actual_result)
        
        def test_mock_remove_one(self):
            app.ordenate_list = MagicMock()
            app.ordenate_list.return_value = [0,1,2,3,4,5,6,7]

            source_list = [2,0,5,3,1,4,6]
            expected_result = [0,1,2,3,4,5,6]

            actual_result = app.remove_one(source_list)

            self.assertListEqual(expected_result, actual_result)
