from textnode import *
import re

def split_nodes_delimiter(old_nodes,delimiter,text_type):

    split_nodes_list = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            split_nodes_list.append(node)
            continue

        str_list = node.text.split(delimiter)
    
        new_node_list = []
        for split_str in str_list:
            if str_list.index(split_str) % 2 == 1:
                new_node_list.append(TextNode(split_str, text_type,))
            else:
                new_node_list.append(TextNode(split_str, TextType.TEXT,))
        
        split_nodes_list.extend(new_node_list)
    
    return split_nodes_list

def extract_markdown_images(text):
    """
    Takes raw markdown text and returns a list of tuples.
    Each tuple should contain the alt text and URL of markdown images
    """

    # match_alt_text = re.findall(r"\[(.*?)\]", text)
    match_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    # return_list = []
    # for i in range(len(match_alt_text)):
    #     return_list.append((match_alt_text[i], match_images[i]))

    return match_images


def extract_markdown_links(text):
    # match_anchor_text = re.findall(r"\[(.*?)\]", text)
    match_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    # return_list = []
    # for i in range(len(match_anchor_text)):
    #     return_list.append((match_anchor_text[i], match_links[i]))

    return match_links

def split_nodes_image(old_nodes):
    split_nodes_list = []
    for node in old_nodes:
    
        if node.text_type != TextType.TEXT:
            split_nodes_list.append(node)
            continue

        match_images = extract_markdown_images(node.text)
        if match_images == ():
            continue
    
        node_text = node.text
        new_node_list = []
        for image in match_images:
            sections = node_text.split(f"![{image[0]}]({image[1]})",1)
            if len(sections) != 2:
                raise ValueError('Image not found in text')
            if sections[0] != '':
                new_node_list.append(TextNode(sections[0], TextType.TEXT,))
            new_node_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = sections[1]
        if node_text != '':
            new_node_list.append(TextNode(node_text, TextType.TEXT,))
        split_nodes_list.extend(new_node_list)
    
    return split_nodes_list

def split_nodes_link(old_nodes):
    split_nodes_list = []
    for node in old_nodes:
    
        if node.text_type != TextType.TEXT:
            split_nodes_list.append(node)
            continue

        match_links = extract_markdown_links(node.text)
        if match_links == ():
            continue
    
        node_text = node.text
        new_node_list = []
        for link in match_links:
            sections = node_text.split(f"[{link[0]}]({link[1]})",1)
            if len(sections) != 2:
                raise ValueError('Link not found in text')
            if sections[0] != '':
                new_node_list.append(TextNode(sections[0], TextType.TEXT,))
            new_node_list.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = sections[1]
        if node_text != '':
            new_node_list.append(TextNode(node_text, TextType.TEXT,))
        split_nodes_list.extend(new_node_list)
    
    return split_nodes_list


def text_to_textnodes(text):

    initial_node = TextNode(text,TextType.TEXT,)
    link_split_nodes = split_nodes_link([initial_node])
    image_split_nodes = split_nodes_image(link_split_nodes)
    code_split_nodes = split_nodes_delimiter(image_split_nodes,'`',TextType.CODE)
    bold_split_nodes = split_nodes_delimiter(code_split_nodes,'**',TextType.BOLD)
    total_split_nodes = split_nodes_delimiter(bold_split_nodes,'*',TextType.ITALIC)

    return total_split_nodes
