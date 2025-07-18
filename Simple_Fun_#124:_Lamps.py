def lamps(a):
    pattern_0 = []
    pattern_1 = []
    count1 = 0
    count2 = 0

    ################ To build the array in ascending of sequence 0,1,0,1,... order #######################

    for i in range(len(a)):
        value = i % 2
        pattern_0.append(value)
    #print(pattern_0)
    for j in range(len(a)):
        if(a[j]!=pattern_0[j]):
            count1+=1
    #print(count1)

    ################To build the array in ascending of sequence  1,0,1,0,... order #######################

    for i in range(len(a)):
        value = (i+1) % 2
        pattern_1.append(value)
    #print(pattern_1)
    for j in range(len(a)):
        if(a[j]!=pattern_1[j]):
            count2+=1
    #print(count2)
    count = min(count1,count2)
    return count


a = lamps([1,0,0,1,1,0,0,0,0,1,0])
print(a)
#c = 1 % 2
#print(c)