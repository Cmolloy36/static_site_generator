import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_tag_eq(self):
        node = HTMLNode('p')
        node2 = HTMLNode('p')
        self.assertEqual(node, node2)

    def test_value(self):
        node = HTMLNode(value="This is a node value")
        node2 = HTMLNode(value="This is a node value")
        self.assertEqual(node, node2)

    def test_children(self):
        children_nodes = [HTMLNode('<p>')]
        node = HTMLNode(children=children_nodes)
        node2 = HTMLNode(children=children_nodes)
        self.assertEqual(node, node2)

    def test_children2(self):
        # 2 different children
        node = HTMLNode(children=[HTMLNode('<p>')])
        node2 = HTMLNode(children=[HTMLNode('<t>')])
        self.assertNotEqual(node, node2)

    def test_props(self):
        test_dict = {'Alice':3, 'Bob':4, 'Cooper':5}
        node = HTMLNode(props=test_dict)
        node2 = HTMLNode(props=test_dict)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
