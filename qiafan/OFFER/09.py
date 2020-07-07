class CQueue:

    def __init__(self):
        self.append_stack = []
        self.delete_stack =[]

    def appendTail(self, value: int) -> None:
        self.append_stack.append(value)

    def deleteHead(self) -> int:
        if len(self.append_stack) == 0:
            return -1
        while self.append_stack:
            self.delete_stack.append(self.append_stack.pop())
        res = self.delete_stack.pop()
        while self.delete_stack:
            self.append_stack.append(self.delete_stack.pop())
        return res



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()