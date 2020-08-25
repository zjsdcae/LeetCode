class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def add(self,x):
        self.s1.append(x)
        
    def poll(self):
        while(self.s1):
            self.s2.append(self.s1.pop())
        res = self.s2.pop()
        while(self.s2):
            self.s1.append(self.s2.pop())
        return res
    
    def peek(self):
        while(self.s1):
            self.s2.append(self.s1.pop())
        res = self.s2[-1]
        while(self.s2):
            self.s1.append(self.s2.pop())
        return res

n = input()
q = Queue()
for _ in range(int(n)):
    input_ = input().split()
    if len(input_) == 1:
        if input_[0] == "peek":
            print(q.peek())
        else:
            q.poll()
    if len(input_) == 2:
        q.add(input_[1])