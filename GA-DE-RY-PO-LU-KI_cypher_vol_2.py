
###### Static Solution #############

def encode(message, _key):
    encoded = []
    custom = {"g": "a", "d": "e", "r": "y", "p": "o", "l": "u", "k": "i", "G": "A", "D": "E", "R": "Y", "P": "O",
              "L": "U", "K": "I", "a": "g", "e": "d", "y": "r", "o": "p", "u": "l", "i": "k", "A": "G", "E": "D",
              "Y": "R", "O": "P", "U": "L", "I": "K"}
    custom1 = {"p": "o", "o": "p", "P": "O", "O": "P", "l": "i", "i": "l", "L": "I", "I": "L", "t": "y", "y": "t",
               "T": "Y", "Y": "T", "k": "a", "a": "k", "K": "A", "A": "K", "r": "e", "e": "r", "R": "E", "E": "R",
               "n": "u", "u": "n", "N": "U", "U": "N"}
    custom2 = {"k": "a", "a": "k", "K": "A", "A": "K", "c": "e", "e": "c", "C": "E", "E": "C", "m": "i", "i": "m",
               "M": "I", "I": "M", "n": "u", "u": "n", "N": "U", "U": "N", "t": "o", "o": "t", "T": "O", "O": "T",
               "w": "y", "y": "w", "W": "Y", "Y": "W"}
    custom3 = {"k": "o", "o": "k", "K": "O", "O": "K", "n": "i", "i": "n", "N": "I", "I": "N", "e": "c", "c": "e",
               "E": "C", "C": "E", "m": "a", "a": "m", "M": "A", "A": "M", "t": "u", "u": "t", "T": "U", "U": "T",
               "r": "y", "y": "r", "R": "Y", "Y": "R"}
    custom4 = {"z": "a", "a": "z", "Z": "A", "A": "Z", "r": "e", "e": "r", "E": "R", "R": "E", "w": "y", "y": "w",
               "W": "Y", "Y": "W", "b": "u", "u": "b", "B": "U", "U": "B", "h": "o", "o": "h", "H": "O", "O": "H",
               "k": "i", "i": "k", "K": "I", "I": "K"}
    custom5 = {"b": "a", "a": "b", "B": "A", "A": "B", "w": "o", "o": "w", "W": "O", "O": "W", "l": "e", "e": "l",
               "L": "E", "E": "L", "t": "y", "y": "t", "T": "Y", "Y": "T", "k": "i", "i": "k", "K": "I", "I": "K",
               "j": "u", "u": "j", "J": "U", "U": "J"}
    custom6 = {"r": "e", "e": "r", "R": "E","E":"R", "g": "u", "u": "g", "G": "U", "U": "G", "l": "a", "a": "l", "L": "A",
               "A": "L", "M": "I", "I": "M", "m": "i", "i": "m", "N": "O", "O": "N", "n": "o", "o": "n", "w": "y",
               "y": "w", "W": "Y", "Y": "W"}
    rule = {"gaderypoluki":custom,
            "politykarenu":custom1,
            "kaceminutowy":custom2,
            "koniecmatury":custom3,
            "zarewybuhoki":custom4,
            "bawoletykiju":custom5,
            "regulaminowy":custom6
            }
    for i in message:
        #print(i)
        if _key in rule:
            if i in rule[_key]:
                z = rule[_key]
                encoded.append(z[i])
            else:
                encoded.append(i)
    return ''.join(encoded)



def decode(message, _key):
    decoded = []
    custom = {"g": "a", "d": "e", "r": "y", "p": "o", "l": "u", "k": "i", "G": "A", "D": "E", "R": "Y", "P": "O",
              "L": "U", "K": "I", "a": "g", "e": "d", "y": "r", "o": "p", "u": "l", "i": "k", "A": "G", "E": "D",
              "Y": "R", "O": "P", "U": "L", "I": "K"}
    custom1 = {"p": "o", "o": "p", "P": "O", "O": "P", "l": "i", "i": "l", "L": "I", "I": "L", "t": "y", "y": "t",
               "T": "Y", "Y": "T", "k": "a", "a": "k", "K": "A", "A": "K", "r": "e", "e": "r", "R": "E", "E": "R",
               "n": "u", "u": "n", "N": "U", "U": "N"}
    custom2 = {"k": "a", "a": "k", "K": "A", "A": "K", "c": "e", "e": "c", "C": "E", "E": "C", "m": "i", "i": "m",
               "M": "I", "I": "M", "n": "u", "u": "n", "N": "U", "U": "N", "t": "o", "o": "t", "T": "O", "O": "T",
               "w": "y", "y": "w", "W": "Y", "Y": "W"}
    custom3 = {"k": "o", "o": "k", "K": "O", "O": "K", "n": "i", "i": "n", "N": "I", "I": "N", "e": "c", "c": "e",
               "E": "C", "C": "E", "m": "a", "a": "m", "M": "A", "A": "M", "t": "u", "u": "t", "T": "U", "U": "T",
               "r": "y", "y": "r", "R": "Y", "Y": "R"}
    custom4 = {"z": "a", "a": "z", "Z": "A", "A": "Z", "r": "e", "e": "r", "E": "R", "R": "E", "w": "y", "y": "w",
               "W": "Y", "Y": "W", "b": "u", "u": "b", "B": "U", "U": "B", "h": "o", "o": "h", "H": "O", "O": "H",
               "k": "i", "i": "k", "K": "I", "I": "K"}
    custom5 = {"b": "a", "a": "b", "B": "A", "A": "B", "w": "o", "o": "w", "W": "O", "O": "W", "l": "e", "e": "l",
               "L": "E", "E": "L", "t": "y", "y": "t", "T": "Y", "Y": "T", "k": "i", "i": "k", "K": "I", "I": "K",
               "j": "u", "u": "j", "J": "U", "U": "J"}
    custom6 = {"r": "e", "e": "r", "R": "E","E":"R", "g": "u", "u": "g", "G": "U", "U": "G", "l": "a", "a": "l", "L": "A",
               "A": "L", "M": "I", "I": "M", "m": "i", "i": "m", "N": "O", "O": "N", "n": "o", "o": "n", "w": "y",
               "y": "w", "W": "Y", "Y": "W"}
    rule = {"gaderypoluki": custom,
            "politykarenu": custom1,
            "kaceminutowy": custom2,
            "koniecmatury": custom3,
            "zarewybuhoki": custom4,
            "bawoletykiju": custom5,
            "regulaminowy": custom6
            }
    for i in message:
        # print(i)
        if _key in rule:
            if i in rule[_key]:
                z = rule[_key]
                decoded.append(z[i])
            else:
                decoded.append(i)
    return ''.join(decoded)

a = encode("Gug hgs g cgt","gaderypoluki")
print(a)

b = decode("yHQtBgjR QmoJRsUMqBJSp   YvzjMRpqpPTksslZ DQdZnEsinMEOpX","regulaminowy")
print(b)


######### Dynamic Solution ################

def encode1(message, _key):
    a = _key[0::2] + _key[1::2] # _key[::2] = take every second element of a string.output"k[0] , k[2] , k[4] etc
    #_key[1::2] = _key[1] , _key[3] , _key[5] etc
    #print(a)
    b = _key[1::2] + _key[0::2]
    #print(b)
    c = message.maketrans(a.upper() + a.lower(),b.upper()+b.lower())
    d = message.translate(c)
    return d


def decode1(str, _key):
    return encode(str, _key)

a = encode1("gug hgs g cgt","gaderypoluki")
print(a)

b = decode1("yHQtBgjR QmoJRsUMqBJSp   YvzjMRpqpPTksslZ DQdZnEsinMEOpX","regulaminowy")
print(b)