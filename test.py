import unittest
import main

class TestWine(unittest.TestCase):

    test_list = main.make_wine_list(main.wine_names, main.wine_scores)
    test_instance = test_list[0]

    sorted_list_by_score = []

    # Test if the Wine object's attribute ID is an int
    def test_obj_attr1(self):
        self.assertIsInstance(self.test_instance.id, int)

    # Test if the Wine object's attribute name is a str
    def test_obj_attr2(self):
        self.assertIsInstance(self.test_instance.name, str)

    # Test if the Wine object's attribute score is an int
    def test_obj_attr3(self):
        self.assertIsInstance(self.test_instance.score, int)

    # Test if the wine list length is 5
    def test_list_length(self):
        self.assertEqual(len(self.test_list), 5)

if __name__ == "__main__":
    unittest.main()