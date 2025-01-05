import re
from enum import Enum

def markdown_to_blocks(markdown):
    normalized = re.sub(r'\n\s*\n', '\n\n', markdown)
    block_list = normalized.split('\n\n')
    block_list_ret = []
    for block in block_list:
        if block != '':
            block = block.strip()
            line_list = block.split('\n')
            line_list_strip = list(map(str.rstrip,line_list))
            block_list_ret.append('\n'.join(line_list_strip))

    return block_list_ret

def identify_block_type(block):
    lines = block.split('\n')

    if block.startswith(('# ','## ', '### ','#### ','##### ','###### ')):
        return 'heading'
    if block[0:3] == '```' and block[-3:] == '```':
        return 'code'
    if block.startswith('>'):
        for line in lines[1:]:
            if not line.startswith('>'):
                return 'paragraph'
        return 'quote'
    if block.startswith('* ') or block.startswith('- '):
        for line in lines[1:]:
            line = line.lstrip()
            if not (line.startswith('* ') or line.startswith('- ')):
                return 'paragraph'
        return 'unordered_list'
    pattern = r'^\s*\d+\.\s*(.*)'
    match = re.match(pattern,block)
    if match:
        for count, line in enumerate(lines):
            match = re.match(pattern,line)
            if not match:
                return 'paragraph'
        return 'ordered_list'

    return 'paragraph'
