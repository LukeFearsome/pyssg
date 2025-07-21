import unittest

from src.htmlnode import ParentNode,LeafNode

class TestParentNode(unittest.TestCase):
    def test_leaf_to_html_div_p(self):
        node = LeafNode("p", "Hello, world!")
        p_node = ParentNode("div",[node],{"color":"red"})
        self.assertEqual(p_node.to_html(), "<div color=\"red\"><p>Hello, world!</p></div>")

    def test_leaf_to_html_div_p_no_props(self):
        node = LeafNode("p", "Hello, world!")
        p_node = ParentNode("div",[node])
        self.assertEqual(p_node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

if __name__ == "__main__":
    unittest.main()
