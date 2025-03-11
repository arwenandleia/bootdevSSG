import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode,TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bd_ex_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        for i in range(len(new_nodes)):
            self.assertEqual(True,new_nodes[i]==expected_nodes[i])

    def test_bd_ex_2(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is not text with a ", TextType.TEXT),
            TextNode("code block  ", TextType.CODE),
            TextNode(" word df", TextType.TEXT),
        ]
        for i in range(len(new_nodes)):
            self.assertEqual(False,new_nodes[i]==expected_nodes[i])

    def test_italics_1(self):
        node = TextNode("This is text with a _italics_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        for i in range(len(new_nodes)):
            self.assertEqual(True,new_nodes[i]==expected_nodes[i])

    def test_italics_multiple(self):
        node = TextNode("This is text with a _italics_ word and _one_ more", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" word and ", TextType.TEXT),
            TextNode("one", TextType.ITALIC),
            TextNode(" more", TextType.TEXT),
        ]
        for i in range(len(new_nodes)):
            self.assertEqual(True,new_nodes[i]==expected_nodes[i])

    def test_multiple_input_nodes(self):
        node1 = TextNode("This is text with a _italics_ word and _one_ more", TextType.TEXT)
        node2 = TextNode("This is text with a _italics_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1,node2], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" word and ", TextType.TEXT),
            TextNode("one", TextType.ITALIC),
            TextNode(" more", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        for i in range(len(new_nodes)):
            self.assertEqual(True,new_nodes[i]==expected_nodes[i])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


        
            
