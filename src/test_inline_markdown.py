import unittest

from textnode import TextNode, TextType
from inline_markdown import *


class TestSplitDelimeter(unittest.TestCase):
    def test_empty(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text,"")

    def test_multiple_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("`code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        self.assertEqual(len(new_nodes),6)
        self.assertEqual(new_nodes[0].text,"This is text with a ")
        self.assertEqual(new_nodes[3].text,"")
        self.assertEqual(new_nodes[3].text_type,TextType.TEXT)
        
    
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text,"This is text with a ")
        self.assertEqual(new_nodes[0].text_type,TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"code block")
        self.assertEqual(new_nodes[1].text_type,TextType.CODE)
        self.assertEqual(new_nodes[2].text," word")
        self.assertEqual(new_nodes[2].text_type,TextType.TEXT)

    def test_bold(self):
        node = TextNode("This is text with **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text,"This is text with ")
        self.assertEqual(new_nodes[0].text_type,TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"bold")
        self.assertEqual(new_nodes[1].text_type,TextType.BOLD)
        self.assertEqual(new_nodes[2].text," text")
        self.assertEqual(new_nodes[2].text_type,TextType.TEXT)

    def test_italic(self):
        node = TextNode("This is text with *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text,"This is text with ")
        self.assertEqual(new_nodes[0].text_type,TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"italic")
        self.assertEqual(new_nodes[1].text_type,TextType.ITALIC)
        self.assertEqual(new_nodes[2].text," text")
        self.assertEqual(new_nodes[2].text_type,TextType.TEXT)

    def test_italic_multiple(self):
        node = TextNode("This is text with *italic* text *and more here*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text,"This is text with ")
        self.assertEqual(new_nodes[0].text_type,TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"italic")
        self.assertEqual(new_nodes[1].text_type,TextType.ITALIC)
        self.assertEqual(new_nodes[2].text," text ")
        self.assertEqual(new_nodes[2].text_type,TextType.TEXT)
        self.assertEqual(new_nodes[3].text,"and more here")
        self.assertEqual(new_nodes[3].text_type,TextType.ITALIC)


    def test_bold_and_italic(self):
        node = TextNode("This is text with *italic* text and **bold here**", TextType.TEXT)
        temp_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(temp_nodes, "*", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text,"This is text with ")
        self.assertEqual(new_nodes[0].text_type,TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"italic")
        self.assertEqual(new_nodes[1].text_type,TextType.ITALIC)
        self.assertEqual(new_nodes[2].text," text and ")
        self.assertEqual(new_nodes[2].text_type,TextType.TEXT)
        self.assertEqual(new_nodes[3].text,"bold here")
        self.assertEqual(new_nodes[3].text_type,TextType.BOLD)

class TestMarkdownExtraction(unittest.TestCase):
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result[0], ("to boot dev", "https://www.boot.dev"))
        self.assertEqual(result[1], ("to youtube", "https://www.youtube.com/@bootdotdev"))
        
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        self.assertEqual(result[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

class TestImageSplit(unittest.TestCase):
    def test_image(self):
        node2 = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        TextType.TEXT,
        )
        new_nodes2 = split_nodes_image([node2])
        self.assertEqual(new_nodes2,
            [
                TextNode('This is text with a ', TextType.TEXT, None), 
                TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'), 
                TextNode(' and ', TextType.TEXT, None), 
                TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg')]
             )
        

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_non_image(self):
        node2 = TextNode(
        "literalstr",
        TextType.TEXT,
        )
        new_nodes2 = split_nodes_image([node2])
        test_node = TextNode("literalstr", TextType.TEXT,)
        self.assertEqual(new_nodes2[0].text, test_node.text)
        self.assertEqual(new_nodes2[0].text_type, test_node.text_type)
        self.assertEqual(new_nodes2[0].url, test_node.url)
        # self.failureException(new_nodes2,ValueError)


class TestLinkSplit(unittest.TestCase):
    def test_link(self):
        node2 = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        new_nodes2 = split_nodes_link([node2])
        self.assertEqual(new_nodes2,
            [
                TextNode('This is text with a link ', TextType.TEXT, None), 
                TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                TextNode(' and ', TextType.TEXT, None), 
                TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')]
             )
        
class TestTotalSplit(unittest.TestCase):
    def testprovided(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        textnode_list = text_to_textnodes(text)
        self.assertEqual(textnode_list,
                         [
                            TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with an ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" word and a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" and an ", TextType.TEXT),
                            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.TEXT),
                            TextNode("link", TextType.LINK, "https://boot.dev"),
                        ]
                    )

if __name__ == "__main__":
    unittest.main()
