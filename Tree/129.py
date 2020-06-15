def sumNumbers(root):
    self.res = 0

    def dfs(node, temp):
        if not node:
            return
        temp = temp*10 + node.val
        if node.left or node.right:
            self.res += temp
        
        dfs(node.left, temp)
        dfs(node.right, temp)

        temp /= 10
    
    dfs(root, 0)
    return self.res