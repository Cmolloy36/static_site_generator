import unittest

from block_markdown import *
from htmlnode import *
from inline_markdown import *
from textnode import *
from markdown_to_html_node import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

class TestExtractTitle(unittest.TestCase):
    def test_extract_h1(self):
        md = '# here is the header'

        title, content = extract_title(md)
        self.assertEqual(title,'# here is the header')
        self.assertEqual(content,'')

    
    def test_no_h1(self):
        md = '''## here is no the header
extra
extra2'''
        with self.assertRaises(Exception):
            self.extract_title(md)

    def test_lower_h1(self):
        md = '''trext
        text
    # here is the header
extra
extra2'''
        title, content = extract_title(md)
        self.assertEqual(title,'here is the header')  
        self.assertEqual(content,'''trext
        text
extra
extra2''')    

    def test_preserves_other_hashtag(self):
        md = '''trext
        text
    # # here is the header
extra
extra2'''
        title, content = extract_title(md)
        self.assertEqual(title,'# here is the header')
        self.assertEqual(content,'''trext
        text
extra
extra2''')      