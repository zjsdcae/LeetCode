def plusOne(digits):
    idx,flag = len(digits)-1,0
    if digits[idx] < 9:
        digits[idx] += 1
        return digits
    else:
        while digits[idx]+1 == 10 and idx >= 0:
            flag = 1
            digits[idx] = 0
            idx -= 1
        if idx == -1 and flag == 1:
            digits.insert(0,1)
        else:
            digits[idx] += 1
        return digits