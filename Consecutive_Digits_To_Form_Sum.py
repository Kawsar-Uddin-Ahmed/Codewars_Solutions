def consecutive_ducks(n):
    result = []
    for start in range(1,n):
        total = 0
        num = []
        for i in range(start,n):
           total+=i
           num.append(i) #Yes — the values added to nums are temporary for that iteration of the outer
                         # loop, because nums is re-created every time the outer loop runs.
           if(total == n):
               result.append(num)
               break
           elif(total > n):
               break
    #print(result)
    #a = sorted(result)
    #b = list(range(min(result), max(result)+1)) #Here I will create a list that will be sorted from minimum to maximum number
    if (result): # It is finding whether the array elements are sorted or not.
        return True
    else:
        return False


v = consecutive_ducks(512)
print(v)


         #******************************** Second Solution ***********************************#
         
def consecutive_ducks(n):
    return (n & (n - 1)) != 0 # Here, I have utilized bit and gate technology from computer science. Here I have
                              #used an AND gate operation between n, n-1. Here, the n and n-1 numbers will be changed
                              # into 0, 1 bit, and then perform the AND operation.
                              #Now, if the result of the AND operation is zero,  then n is a power of 2 and
                              # non-consecutive ducks. (means adding consecutive numbers, you can't get the number)

v = consecutive_ducks(755)
print(v)
