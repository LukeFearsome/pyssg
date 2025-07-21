import unittest

from src.textnode import TextNode,TextType,textnode_to_htmlnode

class TestTextToHtmlNode(unittest.TestCase):
    def test_plaintext(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("link text",TextType.LINK,"archlinux.org")
        htmlnode = textnode_to_htmlnode(node)
        self.assertEqual(htmlnode.tag,'a')
        self.assertEqual(htmlnode.value,"link text")
        self.assertEqual(htmlnode.props,{"href":"archlinux.org"})
    def test_image(self):
        node = TextNode("alt text",TextType.IMAGE,"smile.jpg")
        htmlnode = textnode_to_htmlnode(node)
        self.assertEqual(htmlnode.tag,"img")
        self.assertEqual(htmlnode.props,{"src":"smile.jpg","alt":"alt text"})
if __name__ == "__main__":
    unittest.main()
