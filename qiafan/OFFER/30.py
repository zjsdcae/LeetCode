class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a, self.b = [], []

    def push(self, x: int) -> None:
        self.a.append(x)
        if not self.b or self.b[-1] >= x:
            self.b.append(x)

    def pop(self) -> None:
        res = self.a.pop()
        if res == self.b[-1]:
            self.b.pop()

    def top(self) -> int:
        return self.a[-1]

    def min(self) -> int:
        return self.b[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.s = []


#     def push(self, x: int) -> None:
#         self.s.append(x)

#     def pop(self) -> None:
#         self.s.pop()

#     def top(self) -> int:
#         return self.s[-1]

#     def min(self) -> int:
#         return min(self.s)
