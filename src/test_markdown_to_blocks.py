import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_bd_ex_1(self):
        input_markdown = '''
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
'''
        expected_output = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
            '- This is the first list item in a list block\n- This is a list item\n- This is another list item'

        ]
        fn_output = markdown_to_blocks(input_markdown)
        self.assertListEqual(expected_output,fn_output)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_bd_multiple_newlines(self):
        input_markdown = '''
# This is a heading



This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
'''
        expected_output = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
            '- This is the first list item in a list block\n- This is a list item\n- This is another list item'

        ]
        fn_output = markdown_to_blocks(input_markdown)
        self.assertListEqual(expected_output,fn_output)

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
