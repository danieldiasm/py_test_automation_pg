from unittest import TestCase

from models.item import ItemModel


class UnitTestItemModel(TestCase):

    def setUp(self) -> None:
        self.item_model = ItemModel('Test Item', 10.0)

    # Test Instance Creation
    def test_create_instance(self):
        self.assertIsInstance(self.item_model, ItemModel)

    # Test Instance Constructor values consistency
    def test_create_item(self):
        self.assertEqual(self.item_model.name, 'Test Item',
                         "Item name does not match the constructor argument")
        self.assertEqual(self.item_model.price, 10.0,
                         "Item price does not match the constructor argument")
    # Test JSON
    def test_json(self):
        json_result = self.item_model.json()
        self.assertEqual(json_result, {'name': 'Test Item', 'price': 10.0})

    # The DB should be mocked to work or run as integration tests
    # I've written those tests as well, but the DB became a problem.
    # # Test Save to DB
    # def test_save_to_db(self):
    #     self.item_model.save_to_db()
    #
    # # Test find by name
    # def test_find_by_name(self):
    #     item_found = ItemModel.find_by_name('Test Item')
    #     self.assertEqual(item_found.name, 'Test Item')
    #     self.assertEqual(item_found.price, 10.0)
    #
    # # Test Delete from DB
    # def test_delete_from_db(self):
    #     self.item_model.delete_from_db()
