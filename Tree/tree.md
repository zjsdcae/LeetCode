# Tree Notes

###definition
```python
Node {
    value: any 
    left: Node | null
    right: Ndoe | null
}

preorder(root){
    if root:
        doSomething(root)
        preorder(root.left)
        preorder(root.right)
}

inorder(root){
    if root:
        inorder(root.left)
        dosomething(root)
        inorder(root.right)
}

postorder(root){
    if root:
        postorder(root.left)
        postorder(root.right)
        dosomething(root)
}



```

