# c = 0 

# def add():
#     global c
#     c = c + 2 
#     print(c)

# add()
# print(c)





# def evenOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")
 
 
# # Driver code to call the function
# evenOdd(2)
# evenOdd(3)


# def add(num1,num2):
#     return num1+num2
# def sub(a,b):
#     print(add(number1,number2))
#     return a-b
# def mult(c,e):
#     print(sub(number1,number2))
#     return c*e
# number1=int(input("any number"))
# number2=int(input("any number"))
# print(mult(number1,number2))



# def fac():
#     i=1
#     b=[]
#     while i<user:
#         if user%i==0:
#             b.append(i)
#         i+=1
#     return(b)
# user=int(input("any number"))
# (fac())











a=[12,34,34,56,78,98,87,76,57,67,57,78,56]

def maximum(a):
    max=0
    i=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    return max,[12,34,34,56,78,98,87,76,57,67,57,78]
print(maximum(a))

def dupli(list):
    i=0
    b=[]
    while i<len(list):
        if list[i] not in b:
            b.append(list[i])
        i+=1
    return b
print(dupli(a))







# def fun1():
#     fun1.var = 100
#     print(fun1.var)

# def fun2():
#     print(fun1.var)

# fun1()
# fun2()

# print(fun1.var)


