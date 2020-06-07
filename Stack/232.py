class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stk = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        temp = [] 
        while len(self.stk) > 0:
            temp.append(self.stk.pop())
        self.stk.append(x)
        while len(temp) > 0:
            self.stk.append(temp.pop())      

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stk.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stk[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stk) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()