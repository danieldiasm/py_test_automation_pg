

from unittest import TestCase
from unittest.mock import MagicMock

import sample_basic.app as app


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
