# write code to delete the root in a binary search tree

class Node:
    def __init__(self, data):
        self.data= data
        self.right= None
        self.left= None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def delete(self, root, node):
        if self.root is None: # if there's no root, then it means the tree is empty
            print("The tree is empty.")
            return
        else:
            # find the inorder successor to replace the value of the root, it's the leftmost node in the right subtree
            # then copy the value of the successor node and replace the original value of the top root with it
            root.data= self.find_left(node).data
            successor= self.find_left(node)
            # in case the successor is not a leaf but has a right child, find the parent of the successor
            if successor.right is not None:
                parent= self.find_parent(self.root, successor)
                # in case the successor happens to be the left child of its parent
                if parent.left == successor:
                    parent.left= successor.right # make the successor's right child the left child of the successors parent
                # in case the successor is the right child of its parent as is the case when the successor happens to be the right subtree with no left child , then it's going to be the successor per the logic of find_left method 
                elif parent.right== successor: 
                    parent.right= successor.right # make the right child of the successor the right child of the parent
            else: # if the successor happens to be a leaf, delete it whether it's the left child of its parent or the right child
                if parent.left == successor: 
                    parent.left = None
                elif parent.right == successor:
                    parent.right= None


    # this recursive method keeps going left until it reaches the leftmost node. It starts from the top and keep going downward
    def find_left(self, node):
        if node.left is None: # if the node in the last level has no left child, then it's the leftmost node so we return it since we found it
            return node
        return self.find_left(node.left) # else, keep repeating this method, going one level down with each repetetion till the leftmost node is found
    
    # this recursive method keeps going one level downward till it finds the parent of the leftmost node
    def find_parent(self,root, node):
        if root.left == node or root.right==node: # if the successor happens to be the left child or the right child of the top root, then it means the root is the parent(root) so return it
            return root
        # if the tree consists of many levels, keep checking if the value of the leftmost node (successor) is less than the value of the parent.
        if node.data < root.data:
            return self.find_parent(root.left, node) # if it has a value lesser than that of its parent then it means the successor is the left child of its parent so the parent is root.left.
        else:
            return self.find_parent(root.right, node)# if it's bigger than the value of the parent, it means it's the right child so the parent is root.right.




