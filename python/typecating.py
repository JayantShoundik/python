# example of Implicit type casting 
a=9  # it is an int data type
print(type(a))
b=2.6 # it is an float data type
print(type(b))
print(a+b,type(a+b))  # the result of this data type can be seen is float and that is done by python to  aoid any data loss 
                       # it is type of implicit type conversion // of type casting
#example of Explicit type casting
a=9  # it is an int data type
print(type(a))
b=2.6 # it is an float data type
print(str(a)+str(b),type(b)) 

""" output"""               
# '''<class 'int'>
# <class 'float'>
# 11.6 <class 'float'>
# <class 'int'>
# <class 'float'>
# 92.6
# <class 'float'>
# print(str(a)+str(b))  
# print(type(a+b)) '''                
""" lets see when python get irrited"""
a="ram"
b="ji"
print(int(a)+int(b))    #invalid literal for int() with base 10: 'ram              
            