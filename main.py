a=29
b=99

# Arithmetic
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)

# Relational
print("a>b:",a>b)
print("a<b:",a<b)
print("a==b:",a==b)

# Logical
print("(a>0 and b>0):",a>0 and b>0)
print("(a>0 or b>0):",a>0 or b>0)
print("not (a>0):",not(a>0))

#Assignment 
x=a
print("Initial x:",x)
x+=b
print("x+=b:",x)
x-=b
print("x-=b:",x)
x*=b
print("x*=b:",x)
if b!=0:
    x/=b
    print("x/=b:",x)
