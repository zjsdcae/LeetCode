class Stack():
    def __init__(self):
        self.s = []
        self.smin = []
        
    def push(self,x):
        self.s.append(x)
        if len(self.smin) > 0:
            if self.smin[-1] > x:
                self.smin.append(x)
            else:
                self.smin.append(self.smin[-1])
        else:
            self.smin.append(x)
    
    def pop(self):
        res = self.s[-1]
        del self.s[-1]
        del self.smin[-1]
        return(res)
    
    def getMin(self):
        return self.smin[-1]

n = int(input())
stack = Stack()
for _ in range(n):
    input_ = input().split()
    if len(input_) == 2:
        stack.push(int(input_[1]))
    elif input_[0] == 'pop':
        stack.pop()
    else:
        res = stack.getMin()
        print(res)