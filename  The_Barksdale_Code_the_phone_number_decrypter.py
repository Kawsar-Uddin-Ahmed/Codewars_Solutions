def decode(strng):
    doc = {"1":"9","2":"8","3":"7","4":"6","5":"0","9":"1","8":"2","7":"3","6":"4","0":"5"}
    c = []
    for i in strng:
        if i in doc:
            c.append(doc[i])
    a = ''.join(c)
    return a

a = decode("4103432323") #"6957678787"6957678787....4103432323
print(a)