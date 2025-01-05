from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *
from markdown_to_html_node import *
from copy_contents import *
from generate_page import *

def main():
    md = """#### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

1. This is the first list item in an ordered list block
2. This is an ordered list item
3. This is another ordered list item


1. This is the first list item in an **almost** ordered list block
1. This is an **almost** ordered list item
3. This is another **almost** ordered list item

```this is multiline
code text```"""

    result = markdown_to_html_node(md)
    # print(result)


    # Test Ch5L1
    dest = 'public'
    source = 'static'
    copied_file_list = copy_contents(source,dest)

    from_path = 'content/index.md'
    template_path = 'template.html'
    dest_path = 'public/index.html'
    generate_page(from_path,template_path,dest_path)


    # # Test Ch2
    # first_obj = textnode.TextNode('This is an image node', textnode.TextType.IMAGE, 'https://www.boot.dev/lessons/80ddb6c5-8324-4850-a28c-0c6207596857')
    # obj = first_obj.text_node_to_html_node()
    # print(obj.to_html())
    # print(first_obj.__repr__())

    # lfnd = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(lfnd.props_to_html())
    # print(lfnd.to_html())

    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ],
    # )

    # print(node.to_html())

    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # # print(node.text_type)
    # new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # print(new_nodes[0].text)
    
    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))

    # node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    #     )
    # new_nodes = split_nodes_link([node])
    # print(new_nodes)
    
    # node2 = TextNode(
    #     "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    #     TextType.TEXT,
    # )
    # new_nodes2 = split_nodes_image([node2])
    # print(new_nodes2)

    ### Test Ch3L6
    # txt = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    # node_list = text_to_textnodes(txt)
    # print(node_list)

    ### Test Ch4L1
#     md = """# This is a heading

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item"""
#     blocks = markdown_to_blocks(md)
#     print(blocks)
#     print('\n')


#     md = """# Heading

# * List item 1
#     * Indented item
# * List item 2

# > A blockquote
# > with multiple lines"""
#     blocks = markdown_to_blocks(md)
#     print(blocks)
#     print('\n')

#     md = ""
#     blocks = markdown_to_blocks(md)
#     print(blocks)
#     print('\n')


    ### Test Ch4L2
#     md = """# This is a heading"""
#     blocks = markdown_to_blocks(md)
#     for block in blocks:
#         print(identify_block_type(block))
#     print('\n')

#     md = """# Heading

# * List item 1
#     * Indented item
# * List item 2

# > A blockquote
# > with multiple lines"""
#     blocks = markdown_to_blocks(md)
#     print(blocks)
#     for block in blocks:
#         print(identify_block_type(block))
#     print('\n')

if __name__ == '__main__':
    main()
