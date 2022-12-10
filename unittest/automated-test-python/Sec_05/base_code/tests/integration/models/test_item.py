from models.item import ItemModel  # This has the DB Model in it, enabling the DB to be tested
from tests.base_test import BaseTest  # This module has the setUp and tearDown methods inside it.


class ItemTest(BaseTest):

    def test_crud(self):
        with self.app_context():
            item = ItemModel('Test_Item', 19.99)

            self.assertIsNone(ItemModel.find_by_name('Test_Item'),
                              f"Found an item with name {item.name}, but expected not to.")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Test_Item'),
                                 f"Unable to find the item {item.name}, but expected to.")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('Test_Item'),
                              f"Found an item with name {item.name}, expected to have been deleted.")
