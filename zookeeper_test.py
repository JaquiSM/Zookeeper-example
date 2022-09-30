import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    def test_show_data(self):
        tree = Ztree()
        tree.create('/node4', 'test', True, True, 20, '/')
        self.assertEqual(tree.showNode('/node4'), None)  

    def test_doesnt_exist(self):
        tree = Ztree()
        tree.create('/node2', 'test', True, False, 20, '/')
        self.assertNotEqual(tree.getData('/node3'), 'test')     

    def test_create_node_false(self):
        tree = Ztree()
        tree.create('/node2', 'test', False, False, 20, '/')
        self.assertEqual(tree.getData('/node2'), 'test') 
    
    def test_delete_node(self):
        tree = Ztree()
        tree.create('/node1/node2/node3', 'test', True, False, 20, '/')
        self.assertFalse(tree.delete('/node3', 0))
    
    def test_children(self):
        tree = Ztree()
        tree.create('/node3', 'test', True, False, 20, '/')
        self.assertEqual(tree.getChildren('/node3'), None)

if __name__ == '__main__':
    unittest.main()

