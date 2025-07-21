# Binary Search Tree Deletion Exercise

This exercise implements the **delete** operation for a **binary search tree (BST)**, specifically focusing on deleting the root node and using the **inorder successor** to replace it.

### Steps:

1. **Find the inorder successor** (the leftmost node in the right subtree of the root).
2. **Replace the root’s value** with the value of the inorder successor.
3. **Delete the successor node**:
   - If the successor has a **right child**, it is replaced by that right child.
   - If the successor is a **leaf**, it is removed from the tree.

### Notes:
- The tree structure is updated based on the inorder successor.
- We handle the edge case where the successor has no right child (leaf node).
  
### Example:
Before deletion:

  10
 /  \
5   15
    /
  12
  
After replacing the root with the successor’s value and deleting the successor node:

  12
 /  \
5   15
