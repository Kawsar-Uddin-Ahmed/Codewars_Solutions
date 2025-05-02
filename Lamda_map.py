def square(n,m):
    return n * m
numbers = [1,2,3,4,5,6,7]
most = 5

squared_number = map(lambda x:square(x,most),numbers) #here lambda x is value of function that have.
#Here square(x,most) is inside the lamda function.
# #numbers are the array  and x is the single element of that array.from numbers x values come.
print(list(squared_number))