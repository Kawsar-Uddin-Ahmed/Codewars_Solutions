def scratch(lottery,):
    array = []
    result = 0
    for i in lottery:
        parts = i.split() # Every bunch of string has been made array.
        #print(parts[0]) # From every array writing the first element
        #print(parts[1])
        if(parts[0] == parts[1] == parts[2]): # Comparing each array's each element internally with each other.
            array.append(int(parts[3]))
    for add in array:
        result+=add
    return(result)

a = scratch(["tiger tiger tiger 100","rabbit dragon snake 100","rat ox pig 1000","dog cock sheep 10","horse monkey rat 5","dog dog dog 1000"])
print(a)