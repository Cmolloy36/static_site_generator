import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text nod", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url1(self):
        node = TextNode("This is a text node", TextType.ITALIC,'https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1')
        node2 = TextNode("This is a text node", TextType.ITALIC,'https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee')
        self.assertNotEqual(node, node2)

    def test_font(self):
        node = TextNode("This is a text node", TextType.ITALIC,'https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1')
        node2 = TextNode("This is a text node", TextType.LINK,'https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1')
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()
