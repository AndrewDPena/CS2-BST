import unittest

'''
Description:
Author: Andrew Peña
Version: 1
Help received from: Stack Overflow for While Loop implementation of BFS
https://stackoverflow.com/questions/1894846/printing-bfs-binary-tree-in-level-order-with-specific-formatting
Help provided to: Kelly Trujillo, Ze Liu
'''

class binary_search_tree:
    def __init__ (self, init=None):
        self.__value = self.__left = self.__right = self.__descendants = None

        if init:
            for i in init:
                self.add(i)

    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield(node)

        yield(self.__value)

        if self.__right:
            for node in self.__right:
                yield(node)

    def __str__(self):
        return(','.join(str(node) for node in self))

    def add(self, value):
        if self.__value is None:
            self.__value = value
            height = 1
        elif value < self.__value:
            if not self.__left:
                self.__left = binary_search_tree()
            height = 1 + self.__left.add(value)
        else:
            if not self.__right:
                self.__right = binary_search_tree()
            height = 1 + self.__right.add(value)

        if self.__descendants:
            self.__descendants += 1
        else:
            self.__descendants = 1

        return height
        # if this is the first value for this node, just set to node's value
        # if the value is less than this node's value
            # if there isn't a left
                # create a new tree and have left refer to it
            # else
                # make a recursive call
        # else
            #if there isn't a right...


    def preorder(self):
        vals = [self.__value]
        if self.__left:
            vals[len(vals):] = self.__left.preorder()
        if self.__right:
            vals[len(vals):] = self.__right.preorder()
        return vals

    def inorder(self):
        vals = [self.__value]
        if self.__left:
            vals[0:0] = self.__left.inorder()
        if self.__right:
            vals[len(vals):] = self.__right.inorder()
        return vals


    def postorder(self):
        vals = [self.__value]
        if self.__right:
            vals[0:0] = self.__right.postorder()
        if self.__left:
            vals[0:0] = self.__left.postorder()
        return vals

    def BFS(self):
        results = []
        current = [self]
        while current:
            down = []
            for tree in current:
                results.append(tree.__value)
                if tree.__left:
                    down.append(tree.__left)
                if tree.__right:
                    down.append(tree.__right)
            current = down
        return results
        # create a queue with the root element, and an empty list
        # while there are nodes in the queue
            # grab the first one and add it to the result list
            # if there is a node to the left, add that to the queue
            # if there is a node to the right, add that to the queue

    def recursiveBFS(self, trees=None):
        results = []
        if trees == []:
            return trees
        if trees is None:
            trees = [self]
        next_level = []
        for tree in trees:
            results.append(tree.__value)
            if tree.__left:
                next_level.append(tree.__left)
            if tree.__right:
                next_level.append(tree.__right)
        results[len(results):] = self.recursiveBFS(next_level)
        return results

    def rebalance(self, values):
        if self.__value in values:
            self.__value = self.__left = self.__right = None
        if values:
            mid = len(values)//2
            height = self.add(values[mid])
            if values[0:mid]:
                #self.__left = binary_search_tree()
                self.rebalance(values[0:mid])
            if values[mid+1:]:
                #self.__right = binary_search_tree()
                self.rebalance(values[mid+1:])
            return height

    def remove(self, value):
        pass
            # if self is the value to delete
                # if this is a leaf, remove reference to self in parent
                # if there isn't a left, replace self in the parent with the right
                # if there isn't a right, replace self in the parent with the left
                # tricky bit. first, find the right-most of the left hand tree
                # and do a recursive call to remove it
            # else if the value passed in is smaller, recurse to the left
            # else recurse to the right

class test_binary_search_tree (unittest.TestCase):
    '''
           20
          /  \
        10   30
            /  \
           25  35
    '''

    # C level
    def test_empty(self):
        self.assertEqual(str(binary_search_tree()), 'None')
    def test_one(self):
        self.assertEqual(str(binary_search_tree([1])), '1')
    def test_add(self):
        bt = binary_search_tree()
        bt.add(20)
        bt.add(10)
        bt.add(30)
        bt.add(25)
        bt.add(35)
        self.assertEqual(str(bt), '10,20,25,30,35')
    def test_init(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(str(bt), '10,20,25,30,35')

    # B level
    def test_empty_inorder(self):
        self.assertEqual(binary_search_tree().inorder(), [None])
    def test_inorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.inorder(), [10, 20, 25, 30, 35])
    def test_preorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(list(bt.preorder()), [20, 10, 30, 25, 35])
    def test_postorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.postorder(), [10, 25, 35, 30, 20])

    # A level
    def test_empty_BFS(self):
        self.assertEqual(binary_search_tree().recursiveBFS(), [None])
    def test_BFS(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.recursiveBFS(), [20, 10, 30, 25, 35])

    # Extra Credit
    def test_rebalance_empty(self):
        self.assertEqual(str(binary_search_tree().rebalance([])), 'None')
    def test_manual_rebalance(self):
        bt = binary_search_tree([15, 14, 11, 13, 12, 20, 16, 19, 17])
        bt.rebalance(bt.inorder())
        self.assertEqual(bt.preorder(), [15, 13, 12, 11, 14, 19, 17, 16, 20])

    '''
    def test_double_recursion(self):
        bt = BinaryTree([20, 10, 30, 25, 24, 27, 35])
        bt.remove(30)
        self.assertEqual(str(bt), '10,20,24,25,27,35')

    def test_remove_root(self):
        bt = BinaryTree([20, 10, 30, 25, 35])
        bt.remove(20)
        self.assertEqual(str(bt), '10,25,30,35')
    '''

if '__main__' == __name__:
    unittest.main()
