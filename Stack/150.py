class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for c in tokens:
            if c.isdigit(): s.append(int(c))
            else:
                if not c.isdigit() and c[1:].isdigit():
                    s.append(int(c[1:])*-1)
                    continue
                num1 = s.pop()
                num2 = s.pop()
                if c == '+': s.append(num1+num2)
                elif c == '-': s.append(num2-num1)
                elif c == '*': s.append(num1*num2)
                else: s.append(int(num2/num1))
        return s[-1]
