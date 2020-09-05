# Tree Notes

## Definition

```python
class TreeNode:
    def __init(self,x)
    self.val = x
    self.left = None
    self.right = None
```

### PreOrder

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        res.append(root.val)
        if root.left: res += self.preorderTraversal(root.left)
        if root.right: res += self.preorderTraversal(root.right)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res,s = [],[root]
        while s:
            node = s.pop()
            res.append(node.val)
            if node.right: s.append(node.right)
            if node.left: s.append(node.left)
        return res
```

### Inorder

```python 
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        s,p,res,node = [],root,[],root
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                res.append(node.val)
                node = node.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res
```

### Postorder

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res,s = [],[root]
        while s:
            node = s.pop()
            res.append(node.val)
            if node.left: s.append(node.left)
            if node.right: s.append(node.right)
        return res[::-1]
```

### LevelOrder

```python


```