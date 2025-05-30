def encrypt(word, n):
    a = word.lower()
    b = list(word)
    array = []
    for i in b:
        c = ord(i) -97 +1 #To find out which alphabet is which index in english example: a is 1st letter , b os 2nd letter etc
        array.append(c)
    #print(array)
    for d in range(0,n):
        finalarray = [] #you have to put it here otherwise "array = finalarray" will not work.
        for j in array:
            y = j * 3
            z = y - 5
            finalarray.append(z)
        array = finalarray # It will interchange the second for loops finalarray[] values
    finallyarray = array ## Here the changed encrypted_word is stored.This is used because the
                                 #'finallyarray' is a value of only inside first for loop.
    return finallyarray


def decrypt(encrypted_word, n):
    final_word_array = []
    for d in range(0,n):
        finalarray1 = [] #you have to put it here otherwise "encrypted_word = finalarray1" will not work.
        for j in encrypted_word:
            y = j + 5
            z = y // 3
            finalarray1.append(z)
        encrypted_word = finalarray1 # It will interchange the second for loops encrypted_word[] values
    finalarray2 = encrypted_word # Here the changed encrypted_word is stored.This is used because the
                                 #'finalarray1' is a value of only inside first for loop.
    for i in finalarray2:
        a = chr((i + 97)-1) # It will make the ascii number alphabet example : suppose i = 3 for "c" it is
                            # chr((3+97)-1) = chr(99) == 'c'
        final_word_array.append(a)
    return ''.join(final_word_array)

a = encrypt("encrypting", 2)
b =decrypt([20, 5, 19, 20] , 0)
print(a)
print(b)



