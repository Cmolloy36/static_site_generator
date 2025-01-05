import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_node_eq(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text",{"href": "https://www.google.com"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], 
        {"href": "https://www.google.com"}
        )
        node2 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text",{"href": "https://www.google.com"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], 
        {"href": "https://www.google.com"}
        )
        self.assertEqual(node, node2)

    def test_empty_children(self):
        node = ParentNode(
        "p",
        [], 
        {"href": "https://www.google.com"}
        )
        self.assertIsInstance(node,ParentNode)

    def test_empty_tag(self):
        node = ParentNode(None,
            [
            LeafNode("b", "Bold text",{"href": "https://www.google.com"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        {"href": "https://www.google.com"})
        self.failureException(node, ValueError)

    def test_parent_in_children(self):
        children_nodes = [ParentNode('p',
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
            )
            ]
        node = ParentNode('p',children=children_nodes)
        self.assertEqual(node.to_html(), '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>')

    def test_parents_in_children(self):
        children_nodes = [ParentNode('p',
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
            ),
            ParentNode('p',
            [
            LeafNode("b", "Bold text",{"href": "https://www.google.com"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
            )
            ]
        node = ParentNode('p',children=children_nodes)
        self.assertEqual(node.to_html(), '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b href="https://www.google.com">Bold text</b>Normal text<i>italic text</i>Normal text</p></p>')

if __name__ == "__main__":
    unittest.main()
