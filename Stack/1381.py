class CustomStack:

    def __init__(self, maxSize):
        self.stk = [0]*maxSize
        self.pointer = -1

    def push(self, x):
        if self.pointer < len(self.stk)-1:
            self.pointer += 1
            self.stk[self.pointer] = x

    def pop(self) :
        if self.pointer == -1:
            return -1
        else:
            self.pointer -= 1
            return self.stk[self.pointer+1]

    def increment(self, k, val):
        temp = 0
        if self.pointer+1 <= k:
            temp = self.pointer+1
        else:
            temp = k
        for i in range(temp):
            self.stk[i] += val