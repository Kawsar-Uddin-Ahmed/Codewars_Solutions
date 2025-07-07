def folding(a, b):
    array = []
    while a>0 and b>0:
        square_shape = min(a,b)
        strings = str(square_shape)+"x"+str(square_shape)
        array.append(strings)
        if(a>b):
            a = a-b
        else:
            b = b - a
    return(len(array))


#Only one time square_shape variable is used because after filling the if or else condition the value of
# a and b will be the value that are remain after if or else condition and start the while loop again.

c = folding(1000,700)
print(c)