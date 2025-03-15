import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        input_md = '# A simple title'
        expected_op = 'A simple title'
        fn_op = extract_title(input_md)
        self.assertEqual(expected_op,fn_op)

    def test_multiline_title(self):
        input_md = '''
some stuff here
# A simple title
some other stuff here
'''
        expected_op = 'A simple title'
        fn_op = extract_title(input_md)
        self.assertEqual(expected_op,fn_op)
