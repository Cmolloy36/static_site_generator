import re

from block_markdown import *
from htmlnode import *
from inline_markdown import *
from textnode import *


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    block_type_list = []

    block_nodes = []
    for block in blocks:
        block_type = identify_block_type(block)
        block_type_list.append(block_type)

        block_node = block_to_html_node(block,block_type)
        block_nodes.append(block_node)
        # block_nodes.append('\nNext Block:\n')


        
    parent_HTML_node = ParentNode('div',block_nodes)
    return parent_HTML_node
#    '''


#     str_val = '''- hello
# - hi
#     - greetings s'''

#     # print(strip_ul(str_val))

#     str_val = '''1. hello
# 2. hi
#     3. greetings s'''

#    print(strip_ol(str_val))

    # str_val = '''```this is
    # multiple lines
    # of code```'''

    # print(block_to_html_node(str_val,'code'))

def block_to_html_node(block,block_type):
    match block_type:
        case 'heading':
            htag = count_heading(block)
            children_nodes = text_to_children(strip_heading(block))
            return ParentNode(htag,children_nodes)
        case 'code':
            block = strip_code(block)
            children_nodes = text_to_children(block)
            mid_node = ParentNode('code',children_nodes)
            return ParentNode('pre',mid_node)
        case 'paragraph':
            children_nodes = text_to_children(block)
            return ParentNode('p',children_nodes)
        case 'quote':
            stripped_block = strip_quote(block)
            children_nodes = text_to_children(stripped_block)
            return ParentNode('blockquote',children_nodes)
        case 'unordered_list':
            stripped_block = strip_ul(block)
            children_nodes = tag_list_eles(stripped_block)
            return ParentNode('ul',children_nodes)
        case 'ordered_list':
            stripped_block = strip_ol(block)
            children_nodes = tag_list_eles(stripped_block)
            return ParentNode('ol',children_nodes)

def count_heading(block):
    match = re.search(r'#*',block[0:7])
    count = len(match.group(0))
    htag = f'h{count}'
    return htag

def strip_heading(block):
    return block.lstrip('#').strip()

def strip_code(block):
    return block.strip('```')

def strip_quote(block):
    block_lines = block.split('\n')
    new_list = []
    for line in block_lines:
        new_line = line.strip()
        new_line = new_line.lstrip('> ') 
        new_list.append(new_line)
    return ' '.join(new_list)

def strip_ul(block): # flattens all lists, does not maintain indented lists. Come back to this
    block_lines = block.split('\n')
    new_list = []
    for line in block_lines:
        new_line = line.strip()
        if new_line.startswith('-'):
            new_line = new_line.lstrip('- ') 
        else:
            new_line =new_line.lstrip('* ') 
        new_list.append(new_line)
    return '\n'.join(new_list)

def strip_ol(block): # flattens all lists, does not maintain indented lists. Come back to this
    block_lines = block.split('\n')
    new_list = []
    for line in block_lines:
        pattern = r'^\s*\d+\.\s*(.*)'
        match = re.match(pattern,line)
        new_list.append(match.group(1))
    return '\n'.join(new_list)

def tag_list_eles(block):
    block_lines = block.split('\n')
    new_list = []
    for line in block_lines:
        children = text_to_children(line)
        # Create li node with the processed children
        new_list.append(ParentNode('li', children))
    return new_list

def text_to_children(block):
    block = ' '.join(block.split())
    line_text_nodes = text_to_textnodes(block)
    children_nodes = []
    for node in line_text_nodes:
        children_nodes.append(node.text_node_to_html_node())
    return children_nodes

 
# md2 = markdown_to_html_node(md_blockquote)
# print(md2)
# print(type(md2))
# print(md2.to_html())