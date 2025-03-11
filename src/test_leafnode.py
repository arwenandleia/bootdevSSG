import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me",{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, 'This is some raw text')
        self.assertEqual(node.to_html(),'This is some raw text')



if __name__ == '__main__':
    unittest.main()