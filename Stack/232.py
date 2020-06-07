class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stk = []
        self.top = -1
        self.front = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.top += 1
        self.stk.append(x)         

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.front += 1
        return self.stk[self.front-1]

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stk[self.front]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.top+1 == self.front



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()