import unittest

from src.htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("img", "test.jpg", None, {"width": 230, "color": "red"})
        self.assertEqual(repr(node), "HTMLNode img test.jpg None {'width': 230, 'color': 'red'}")
    def test_prop_to_htmll(self):
        node = HTMLNode("test", "value", None, {"width": 230, "color": "red"})
        self.assertEqual(node.props_to_html()," width=\"230\" color=\"red\"")

if __name__ == "__main__":
    unittest.main()