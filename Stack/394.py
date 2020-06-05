def decodeString(s):
    stk = [] 
    num = 0
    res = "" 
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stk.append((res, num))
            res, num = "", 0
        elif c == "]":
            t = stk.pop()
            res = t[0] + res * t[1]
        else:
            res += c
    return res

        # stk = []
        # num = 0
        # res = ""
        # for c in s:
        #     if c.isdigit():
        #         nun = num * 10 + int(c)
        #     elif c == '[':
        #         stk.append((res, num))
        #         res, num = "", 0
        #     elif c == ']':
        #         t = stk.pop()
        #         res = t[0] + res * t[1]
        #     else: 
        #         res += c
        # return res

