def same_structure_as(original,other):
    if type(original) != type(other):
        return False
    if len(original) == len(other) == 0:
        return True
    if len(original)!= len(other):
        return False
    #The loop run until the condition is not matched . any condition is matched the
    #loop will stop and come out but any condition matched it will immediately return
    #the result inside the if or elif condition and come out of the loop immediately
    for i in range(len(original)):
        if bool(type(original[i] )== list) != bool(type(other[i]) == list):
            return False
        elif type(original[i]) == type(other[i]) == list:
            return same_structure_as(original[i],other[i]) #RECURSION IS USED BECAUSE IF ONE
                                                           #ELEMENT IS MATCH THE OTHER MAY NOT
    return True

original = [1,'[',']']
other = ['[',']',1]
or1 = [1,[1,1]]
oth1 = [[2,2],2]
print(same_structure_as(original,other))
print(same_structure_as(or1,oth1))
