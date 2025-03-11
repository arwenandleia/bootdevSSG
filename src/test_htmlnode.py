import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_props_to_html_with_space(self):
        htmlNode = HTMLNode(
            tag='a',
            value='www.google.com',
            props={
                   "href": "https://www.google.com",
                    "target": "_blank",
            })
        props_to_html = htmlNode.props_to_html()
        self.assertEqual(props_to_html,' href="https://www.google.com" target="_blank"')
    
    def test_neq_props_to_html_without_space(self):
        htmlNode = HTMLNode(
            tag='a',
            value='www.google.com',
            props={
                   "href": "https://www.google.com",
                    "target": "_blank",
            })
        props_to_html = htmlNode.props_to_html()
        self.assertNotEqual(props_to_html,'href="https://www.google.com" target="_blank"')
    
    def test_props_to_html_no_props(self):
        htmlNode = HTMLNode(
            tag='a',
            value='www.google.com')
        props_to_html = htmlNode.props_to_html()
        self.assertEqual(props_to_html,'')
    
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


    



if __name__ == "__main__":
    unittest.main()
    
