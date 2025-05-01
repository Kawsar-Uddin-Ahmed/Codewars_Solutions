def decode(code, key):
    arra1 = []
    r =[]
    finalresult = []
    k = str(key)
    arra1 += [int(k1) for k1 in k]
    #for k1 in k: #It is the elaborated form ofthe upper "arra" variable
     #   a = int(k1)
      #  arra1.append(a)
    #print(arra1)
    while len(arra1) < len(code):
        arra1.extend(arra1[:len(code) - len(arra1)])
    r+=[m-arra1[i] for i , m in enumerate(code)]
    #for i , m in enumerate(code):#It is the elaborated form ofthe upper "r" variable
     #   a = m - arra1[i]
     #   r.append(a)
    #print(r)
    finalresult+=[chr(i+96) for i in r]
    print(''.join(finalresult))
    #for i in r: :#It is the elaborated form ofthe upper "finalresult" variable
     #   a = chr(i+96)
      #  finalresult.append(a)
    #print(''.join(finalresult))

a = decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939)
print(a)