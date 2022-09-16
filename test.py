import unittest
import main

class TestWine(unittest.TestCase):

    test_names = ["Chardonnay", "Viognier", "Gewurtztraminer", "Pinot Gris", "Riesling"]
    test_scores = [76, 86, 94, 92, 88]
    test_list = main.make_wine_list(test_names, test_scores)
    test_instance = test_list[0]

    expected_list_by_name = "[0\t76\tChardonnay, 2\t94\tGewurtztraminer, 3\t92\tPinot Gris, 4\t88\tRiesling, 1\t86\tViognier]"
    expected_list_by_score = "[2\t94\tGewurtztraminer, 3\t92\tPinot Gris, 4\t88\tRiesling, 1\t86\tViognier, 0\t76\tChardonnay]"

    # Test if the Wine object's attribute ID is an int
    def test_obj_attr1(self):
        self.assertIsInstance(self.test_instance.id, int, "Wine ID attribute should be an integer")

    # Test if the Wine object's attribute name is a str
    def test_obj_attr2(self):
        self.assertIsInstance(self.test_instance.name, str)

    # Test if the Wine object's attribute score is an int
    def test_obj_attr3(self):
        self.assertIsInstance(self.test_instance.score, int, "Wine score attribute should be an integer")

    # Test if the wine list length is 5
    def test_list_length(self):
        self.assertEqual(len(self.test_list), 5, "Wine object list length should be 5")

    # Test if the sort by name (asc) is correct
    def test_sort_by_name(self):
        test_list_by_name = main.sort_by_name(self.test_list)
        self.assertEqual(self.expected_list_by_name, str(test_list_by_name), "Should be " + self.expected_list_by_name)

    # Test if the sort by score (desc) is correct
    def test_sort_by_score(self):
        test_list_by_score = main.sort_by_score(self.test_list)
        self.assertEqual(self.expected_list_by_score, str(test_list_by_score), "Should be " + self.expected_list_by_score)

if __name__ == "__main__":
    unittest.main()