
def plusone(digits):

    if digits[0] == '0' and len(digits) ==1:
        return digits[0] + 1
    i = len(digits) - 1
    carry = 1
    while i >= 0:
        if digits[i] + carry < 10:
            digits[i] = digits[i] + carry
            break
        else:
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp // 10
            i -= 1
    if i == -1 and carry == 1:
        digits.insert(0,carry)


    [print(digits[j]) for j in range(len(digits)) ]
    return digits

d = [9]
plusone(d)