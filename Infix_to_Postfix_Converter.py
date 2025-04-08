def to_postfix(infix):
    def is_operator(ch):
        return ch in "+-*/%^"
    def get_precedence(op):
        if op == "^":
            return 3
        elif op in "*/%":
            return 2
        elif op in "+-":
            return 1
        else:
            return -1
    postfix =""
    stack = []
    for char in infix:
        if char.isalnum(): #it will be true if the characters are alphanumeric
            postfix+=char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(': # only "stack" means if stack contains any element or not
                                              #and stack[1-] means previous element (last element)
                postfix += stack.pop() #remove the top element of the stack and add it in the postfix string
            stack.pop() #Remove '('
        elif is_operator(char):
            while stack and (get_precedence(char) < get_precedence(stack[-1]) or (get_precedence(char) == get_precedence(stack[-1]) and char != "^")): #here means if the new(top) element in the stack and its power if lesser that the last element the last element will be pop up and add with the postfix .Also the new element will be append in the stack again.
                postfix+=stack.pop()
            stack.append(char)
    while stack:
        postfix+=stack.pop()
    return postfix

#a = to_postfix("5+(6-2)*9+3^(7-1)")
#a = to_postfix("1^2^3")
a = to_postfix("3*3/(7+1)")
print(a)