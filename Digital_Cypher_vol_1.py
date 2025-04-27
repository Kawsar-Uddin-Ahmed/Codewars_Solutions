def encode(message, key):
    b = message.lower()
    d = {}
    arra = []
    result = []
    if (isinstance(key,int) == True):
        d = {chr(i+96):i for i in range(1,27)}
        #for i in range(1,27): #It is the elaborated form ofthe upper "d" variable
         #   v = chr(i+96)
          #  d[v] = i
        #print(d)
        arra+= [d[key1] for j in message for key1 in d if key1 == j]
        #for j in message:  #It is the elaborated form ofthe upper "arra" variable
         #       for key1 in d:
          #          if(key1 == j):
           #             arra.append(d[key1])
        #print(arra)
        k = str(key)
        keyarr = []
        keyarr+=[int(v) for v in k]
        #for v in k:#It is the elaborated form ofthe upper "keyarr" variable
         #   y = int(v)
          #  keyarr.append(y)
        #print(keyarr)
        while len(keyarr) < len(arra):
            keyarr.extend(keyarr[:len(arra) - len(keyarr)]) #[:b] means from beginning to end
        #print(keyarr)
        result+=[m+keyarr[index] for index,m in enumerate(arra)]
        #count = 0
        #for m in arra:
         #   add = m + keyarr[count]
          #  result.append(add)
           # count+=1 #[14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])
        return result
        #for i , m in enumerate(arra):
         #   print(keyarr[i],i,m)

a = encode("masterpiece",1939)
print(a)