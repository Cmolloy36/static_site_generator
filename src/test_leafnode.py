import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_node_eq(self):
        node = LeafNode('p','str text')
        node2 = LeafNode('p','str text')
        self.assertEqual(node, node2)

    def test_value(self):
        node = LeafNode('p',"This is a node value")
        node2 = LeafNode('p',"This is a node value")
        self.assertEqual(node, node2)

    def test_empty_tag(self):
        node = LeafNode(None,value="This is a node value")
        self.assertIsInstance(node.to_html(), str)

    def test_props(self):
        test_dict = {'Alice':3, 'Bob':4, 'Cooper':5}
        node = LeafNode('p',"This is a node value",props=test_dict)
        node2 = LeafNode('p',"This is a node value",props=test_dict)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
