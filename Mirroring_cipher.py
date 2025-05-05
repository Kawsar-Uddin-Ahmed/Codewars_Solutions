def mirror(code,key="abcdefghijklmnopqrstuvwxyz"):
    #key = "abcdefghijklmnopqrstuvwxyz"
    #print(key[6])
    result = ""
    c = code.lower()
    #result=''.join([key[25 - key.index(i)] if i in key else i for i in c]) #As the if..else so the if..else
    #is written before the for loop but if there was only "if" than it will be written after for loop.
    #This formula "key[25 - key.index(i)]" can only be used when all 26 letter are synchronizely in
    #key. As there will be custom key so you have to use the formula: "key[len(key) - 1 - key.index(i)"
    result = ''.join([key[len(key) - 1 - key.index(i)] if i in key else i for i in c])#
    #for i in c: #It is the elaborated form of the upper "result" variable.
     #   if i in key:
      #      ciphering = key[25 - key.index(i)]
       #     result+=ciphering
       # else:
        #    result+=i
    return result
a = mirror("Welcome home")
print(a)

b = mirror("hello", "abcdefgh")
print(b)