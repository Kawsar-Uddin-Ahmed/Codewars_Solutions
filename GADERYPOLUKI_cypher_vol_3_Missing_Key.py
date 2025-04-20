def find_the_key(m, s):
    cipher = set()
    for i in range(len(m)):
        #print(m)
        for j in range(len(m[i])):
            #print(m[i][j])
            if s[i][j] != m[i][j]:
                if (m[i][j] < s[i][j]):
                    cipher.add(m[i][j] + s[i][j]) #it will make m = 'a' , s = 'c' , m+s = 'ac'
                else:
                    cipher.add(s[i][j] + m[i][j])#it will make m = 'd' , s = 'b' , s+m = 'bd'
                    #print(v)
    return ''.join(sorted(cipher))

messages = ['hmqzcpc', 'sgnzebz dbylfch', 'urkjopnps', ',ggozvslk', 'wuaqi']
secrets = ['hmqzcoc', 'sguzrbz dbtifch', 'neajpouos', ',ggpzvsia', 'wnkql']
c = find_the_key(messages,secrets)
print(c)




