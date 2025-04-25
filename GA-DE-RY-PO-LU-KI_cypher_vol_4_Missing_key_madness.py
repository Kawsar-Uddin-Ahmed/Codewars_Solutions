from itertools import permutations

def search_for_key(messages, secrets):
    for perm in permutations(secrets):
        d = {}
        for m,s in zip(messages, perm):
            #print(m,s)
            for x,y in zip(m, s):
                #print(x,y)
                if x != y:
                    #print(d.get(x,y)) #Here d.get(x,y) means y is the value of x.here y is key
                    #print(d.get(y,x)) #Here d.get(y,x) means x is the value of y.here x is key
                    if d.get(x, y) != y or d.get(y, x) != x:
                        break
                    d[x], d[y] = y, x
            else: #THis else if for loop else not if...else.
                #Here the else is used for loop is executed only if
                # the loop completes normally without encountering a break statement.
                continue #continue statement inside this else block immediately jumps to the next
                # iteration of the middle for loop, moving on to the next message-secret pair in the
                # current permutation
            break #This break statement is executed if the else block of the middle loop is not
            # reached. This happens when the inner loop encounters a contradiction and executes its
            # break statement.
        else: #This else if for loop else not if..else.
            #only if the outer loop completes all its iterations without encountering a raise statemen
            return ''.join(sorted({''.join(sorted((k, v))) for k,v in d.items()}))
    raise Exception("No solution for this input")

















a = ["dance", "level", "right", "yours"]
b = ["tpnes", "irvri", "dkucr", "elghy"]
c = search_for_key(a,b)
print(c)