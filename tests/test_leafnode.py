import unittest

from src.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_div(self):
        node = LeafNode("a", "Content.",{"href":"site.com","color":"red"})
        self.assertEqual(node.to_html(),"<a href=\"site.com\" color=\"red\">Content.</a>")
if __name__ == "__main__":
    unittest.main()
