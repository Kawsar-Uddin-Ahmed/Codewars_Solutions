def cake_slice(n):
    a = ((n**2) + n + 2)//2 # I have used Lazy Caterer's Sequence", which calculates the maximum number
                           # of regions a circle can be divided into with n straight lines.Because the cake
                           # is circle
    return a


b = cake_slice(733)
print(b)