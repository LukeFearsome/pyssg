import unittest
from src.markdown_blocks import block_to_blocktype, BlockType  # adjust path if needed

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_blocktype("# Heading 1"), BlockType.H)
        self.assertEqual(block_to_blocktype("## Heading 2"), BlockType.H)
        self.assertEqual(block_to_blocktype("### Subheading"), BlockType.H)

    def test_code_block(self):
        code_block = "```\ndef foo():\n    return 42\n```"
        self.assertEqual(block_to_blocktype(code_block), BlockType.C)

    def test_quote_block(self):
        quote_block = "> This is a quote\n> Spanning two lines"
        self.assertEqual(block_to_blocktype(quote_block), BlockType.Q)

    def test_unordered_list(self):
        ul_block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_blocktype(ul_block), BlockType.UL)

    def test_ordered_list(self):
        ol_block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_blocktype(ol_block), BlockType.OL)

    def test_paragraph(self):
        paragraph = "This is a plain paragraph.\nStill the same paragraph."
        self.assertEqual(block_to_blocktype(paragraph), BlockType.P)

if __name__ == "__main__":
    unittest.main()
