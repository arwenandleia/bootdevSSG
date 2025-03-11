import unittest
from textnode import TextNode,TextType
from textnode_to_htmlnode import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a BOLD node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a BOLD node")
        self.assertEqual(html_node.children, None)

    def test_italic(self):
        node = TextNode("This is a ITALIC node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a ITALIC node")
        self.assertEqual(html_node.children, None)

    def test_code(self):
        node = TextNode("This is a Code block", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a Code block")
        self.assertEqual(html_node.children, None)

    def test_link(self):
        node = TextNode('link to google',TextType.LINK,'www.google.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "link to google")
        self.assertEqual(html_node.children, None)
        self.assertDictEqual(html_node.props,{"href":"www.google.com"})
        
    def test_image(self):
        node = TextNode('google image',TextType.IMAGE,'www.google.com/catpic')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.children, None)
        self.assertDictEqual(html_node.props,{
            "src":"www.google.com/catpic",
            "alt":"google image"
            })
        
    def test_image_bd_sol(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )
