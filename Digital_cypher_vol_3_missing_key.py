def find_the_key(message, code):
    s = []
    v = []
    la = []
    for i in message:
        b = ord(i)
        s+=[b - 96]
    for index , m in enumerate(code):
        if (s[index] > code[index]):
            v+=[s[index] - m]
        else:
            v+=[m - s[index]]
    p = ''.join(str(i) for i in v)
    #print(p)
    #print(len(p))
    for k in range(1, len(p)):
        pattern = p[:k]     # index 0 to k-1
        #print(pattern)
        repeat_len = len(p) // k
        #print(repeat_len)
        repeated = pattern * repeat_len
        #print(repeated)
        if p.startswith(repeated):
        #startswith will see that p starts with 12 and repeated is 121212 so it will take it but if p
        # is 123 at the beginning and repeated is 121212 it will not take it as startswith
            remainder = p[len(repeated):]
            #print(remainder)
            if pattern.startswith(remainder):
                return int(pattern)
    return int(p)









a = find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20])
print(a)