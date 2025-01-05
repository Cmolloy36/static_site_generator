import unittest

from textnode import TextNode, TextType
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_base_case(self):
        md = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks[0],'# This is a heading')
        self.assertEqual(blocks[1],'This is a paragraph of text. It has some **bold** and *italic* words inside of it.')
        self.assertEqual(blocks[2],'''* This is the first list item in a list block
* This is a list item
* This is another list item''')
        
    def test_indented_line(self):
        md = """# Heading

* List item 1
  * Indented item
* List item 2

> A blockquote
> with multiple lines"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks[0],'# Heading')
        self.assertEqual(blocks[1],'''* List item 1
  * Indented item
* List item 2''')
        self.assertEqual(blocks[2],'''> A blockquote
> with multiple lines''')
        
    def test_multiple_indents(self):
        md = """* Level 1
  * Level 2
    * Level 3

> Quote with
  multiple lines
    and indentation

1. Numbered list
   * With mixed
   * Bullet points"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks[0],'''* Level 1
  * Level 2
    * Level 3''')
        self.assertEqual(blocks[1],'''> Quote with
  multiple lines
    and indentation''')
        self.assertEqual(blocks[2],'''1. Numbered list
   * With mixed
   * Bullet points''')
        
    def test_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        md = """# This is a heading"""
        blocks = markdown_to_blocks(md)
        block_type_list = []
        for block in blocks:
            block_type_list.append(identify_block_type(block))
        self.assertEqual(block_type_list,['heading'])

    def test_notheading_unordered_quote(self):
        md = """#Heading

* List item 1
    * Indented item
* List item 2

- List item 1
    - Indented item
* List item 2

- List item 1
    - Indented item
List item 2

> A blockquote
> with multiple lines"""
        blocks = markdown_to_blocks(md)
        block_type_list = []
        for block in blocks:
            block_type_list.append(identify_block_type(block))
        self.assertEqual(block_type_list[0],'paragraph')
        self.assertEqual(block_type_list[1],'unordered_list')
        self.assertEqual(block_type_list[2],'unordered_list')
        self.assertEqual(block_type_list[3],'paragraph')
        self.assertEqual(block_type_list[4],'quote')

    
    def test_heading_ordered_code(self):
        md = """###### Heading

1. List item 1
2. Indented item
3. List item 2

```A blockquote
with multiple lines```"""
        blocks = markdown_to_blocks(md)
        block_type_list = []
        for block in blocks:
            block_type_list.append(identify_block_type(block))
        self.assertEqual(block_type_list[0],'heading')
        self.assertEqual(block_type_list[1],'ordered_list')
        self.assertEqual(block_type_list[2],'code')

    def test_notheading_ordered_notcode(self):
        md = """########### Heading

0. List item 1
1. Indented item
3. List item 2

```code
with multiple lines``"""
        blocks = markdown_to_blocks(md)
        block_type_list = []
        for block in blocks:
            block_type_list.append(identify_block_type(block))
        self.assertEqual(block_type_list[0],'paragraph')
        self.assertEqual(block_type_list[1],'ordered_list')
        self.assertEqual(block_type_list[2],'paragraph')

    def test_notheading_orderedlist_notquote(self):
        md = """########### Heading

1. List item 1
1. Indented item
3. List item 2

> A blockquote
with multiple lines"""
        blocks = markdown_to_blocks(md)
        block_type_list = []
        for block in blocks:
            block_type_list.append(identify_block_type(block))
        self.assertEqual(block_type_list[0],'paragraph')
        self.assertEqual(block_type_list[1],'ordered_list')
        self.assertEqual(block_type_list[2],'paragraph')