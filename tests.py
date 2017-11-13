import unittest
import SearchTree, node

class TestTreeMethods(unittest.TestCase):

    def test_add_first_element(self):
        tree = SearchTree.SearchTree()
        tree.add_data(5)
        self.assertEqual(tree.root.data, 5)

    def test_add_to_right_child(self):
        tree = SearchTree.SearchTree()
        tree.add_data(5)
        tree.add_data(6)
        self.assertEqual(tree.root.right_child.data, 6)

    def test_add_to_left_child(self):
        tree = SearchTree.SearchTree()
        tree.add_data(5)
        tree.add_data(4)
        self.assertEqual(tree.root.left_child.data, 4)

    def test_search_returns_true(self):
        tree = SearchTree.SearchTree()
        tree.add_data(5)
        tree.add_data(4)
        self.assertEqual(tree.search(4), True)

    def test_search_returns_false(self):
        tree = SearchTree.SearchTree()
        tree.add_data(5)
        tree.add_data(4)
        self.assertEqual(tree.search(7), False)

    def test_adds_to_second_right_child(self):
        tree = SearchTree.SearchTree()
        tree.add_data(4)
        tree.add_data(6)
        tree.add_data(7)
        self.assertEqual(tree.root.right_child.right_child.data, 7)

    def test_adds_to_second_left_child(self):
        tree = SearchTree.SearchTree()
        tree.add_data(4)
        tree.add_data(6)
        tree.add_data(7)
        tree.add_data(5)
        self.assertEqual(tree.root.right_child.left_child.data, 5)