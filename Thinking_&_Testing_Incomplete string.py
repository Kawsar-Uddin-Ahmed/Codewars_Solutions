def testit(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    result = ''
    for i in range(0,len(s)-1,2):
        ind1 = alphabet.index(s[i]) #suppose s[i] = 'h' and it is index number is 8 in alphabet.
        ind2 = alphabet.index(s[i+1]) # supose s[i] = 'o' from string "hfehlllmo" the last string.
               # so now there is nothing s[i+1]. So , it will not work the loop will be terminated

        index = (ind1 + ind2) // 2
        result+=alphabet[index]
    if(len(s) % 2 == 0):
        return result
    else:
        a = result + s[-1] # s[-1] last element of array
        return a



print(testit("hfehlllmo"))

