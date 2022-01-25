def fun2(number):
    print (number+2)
    fun1()
def fun1():                          
    print ("Called by main function")
    fun2(4)                              
    
# fun1()

