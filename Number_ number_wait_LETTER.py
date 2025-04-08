import re

def do_math(st):
    b = st.split()
    def get_meth(s):
        a = re.search(r'[a-zA-Z]',s)
        if a:
            return a.group(0).lower() #Finding the alphabetical character.group(0) means return the 1st alphabetical character.

        else:
            return float('inf') #Place strings with no alpha chars at the end.
    m = sorted(b,key=get_meth) #b means the full array and key means the element of the array it will sort the element of the array and  that build the array according ascending order.
    #print(m)
    c = []
    for i in m:
        h = re.sub("[abcdefghijklmnopqrstuvwxyz]","",i)
        j = int(h)
        c.append(j)
    a1 = c
    print(a1)
    l = len(a1)
    #print(l)
    op = ['+','-','*','/']
    op = (op * l)[:len(a1)-1] #It will start from the a1[0] and goes up to a1[last]-1.The amount of op will be total_length_of_a1 - 1
    #print(op)
    result = a1[0]
    for i in range(1,len(a1)):
         operator = op[i-1]
         operand = a1[i]
         if operator == '+':
             result+=operand
         elif operator == '-':
             result-=operand
         elif operator == '*':
             result*=operand
         elif operator == '/':
             result/=operand
    return round(result)

s= "24z6 1z23 y369 89z 900b"
v = do_math(s)
print(v)
