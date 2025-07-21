import unittest
from src.create_html import extract_title


class TestCreateHtml(unittest.TestCase):
    def test_extract_title(self):
        md = "random text\nanother line\n# This is a heading\nand more text"

        self.assertEqual(extract_title(md),"This is a heading")
