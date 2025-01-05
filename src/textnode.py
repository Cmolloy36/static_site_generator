from enum import Enum
from htmlnode import *

TextType = Enum('TextType', ['TEXT', 'BOLD', 'ITALIC', 'CODE', 'LINK', 'IMAGE'])

class TextNode(object):
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        # keep an eye out for this because there may be an issue with the way I call text_type
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None,self.text)
            case TextType.BOLD:
                return LeafNode('b',self.text)
            case TextType.ITALIC:
                return LeafNode('i',self.text)
            case TextType.CODE:
                return LeafNode('code',self.text)
            case TextType.LINK:
                return LeafNode('a',self.text,{'href': self.url})
            case TextType.IMAGE:
                return LeafNode('img','',{'src': self.url, 'alt': self.text})
            case _:
                raise Exception('Not a supported text type')