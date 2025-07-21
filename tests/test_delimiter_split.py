import unittest 

from src.textnode import TextNode, TextType,split_nodes_delimiter

class TestTextToHtmlNode(unittest.TestCase):
    def test_bold_split(self):
        node = TextNode("Testing splitting **bold** text.",TextType.PLAIN)
        split_nodes = split_nodes_delimiter([node],'**',TextType.BOLD) 
        self.assertEqual(split_nodes,
                         [TextNode("Testing splitting ",TextType.PLAIN),
                          TextNode("bold",TextType.BOLD),
                          TextNode(" text.",TextType.PLAIN)])
    
    def test_italic_split(self):
        node = TextNode("Testing splitting *italic* text.",TextType.PLAIN)
        split_nodes = split_nodes_delimiter([node],'*',TextType.ITALIC) 
        self.assertEqual(split_nodes,
                         [TextNode("Testing splitting ",TextType.PLAIN),
                          TextNode("italic",TextType.ITALIC),
                          TextNode(" text.",TextType.PLAIN)])

if __name__ == "__main__":
    unittest.main()
