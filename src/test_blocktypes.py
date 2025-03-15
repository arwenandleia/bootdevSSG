import unittest
from blocktypes import block_to_block_type,BlockType


class TestBlockToBlockTypes(unittest.TestCase):
    def test_headings_1(self):
        input_block = '# This is heading 1'
        expected_output = BlockType.HEADING
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_headings_2(self):
        input_block = '## This is heading 2'
        expected_output = BlockType.HEADING
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_headings_6(self):
        input_block = '###### This is heading 6'
        expected_output = BlockType.HEADING
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_seven_hashes_hence_para(self):
        input_block = '####### This is heading 1'
        expected_output = BlockType.PARAGRAPH
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_simple_code_block(self):
        input_block = '``` Some Code ```'
        expected_output = BlockType.CODE
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_should_not_be_code(self):
        input_block = '`````'
        expected_output = BlockType.PARAGRAPH
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_multiline_code(self):
        input_block = '''
```
some code here
and more code
```
'''
        expected_output = BlockType.CODE
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_simple_quote(self):
        input_block = '>Something Wise goes here'
        expected_output = BlockType.QUOTE
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_quote_multiline(self):
        input_block = '>Something Wise goes here\n>And Plato said'
        expected_output = BlockType.QUOTE
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_not_a_quote(self):
        input_block = '>Something Wise goes here\nAnd Plato said'
        expected_output = BlockType.PARAGRAPH
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_simple_unordered_list(self):
        input_block = '- '
        expected_output = BlockType.UNORDERED_LIST
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_ordered_list(self):
        input_block = '1. First Item\n2. Second Item\n3. Third Item'
        expected_output = BlockType.ORDERED_LIST
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_not_ordered_list(self):
        input_block = '1. First Item\n1. Second Item'
        expected_output = BlockType.PARAGRAPH
        actual_output = block_to_block_type(input_block)
        self.assertEqual(expected_output,actual_output)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    