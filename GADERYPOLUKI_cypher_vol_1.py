def encode(message):
    encoded = []
    custom = {"g":"a","d":"e","r":"y","p":"o","l":"u","k":"i","G":"A","D":"E","R":"Y","P":"O","L":"U","K":"I","a":"g","e":"d","y":"r","o":"p","u":"l","i":"k","A":"G","E":"D","Y":"R","O":"P","U":"L","I":"K"}
    for i in message:
        if i in custom:
            encoded.append(custom[i])
        else:
            encoded.append(i)
    return ''.join(encoded)




def decode(message):
    decoded = []
    custom1 =  {"g":"a","d":"e","r":"y","p":"o","l":"u","k":"i","G":"A","D":"E","R":"Y","P":"O","L":"U","K":"I","a":"g","e":"d","y":"r","o":"p","u":"l","i":"k","A":"G","E":"D","Y":"R","O":"P","U":"L","I":"K"}
    for i in message:
        if i in custom1:
            decoded.append(custom1[i])
        else:
            decoded.append(i)
    return ''.join(decoded)






a = "ABCD"
print(encode(a))

b = "Ala has a cat"
print(decode(b))