# -***********************Operators
print("-*********************** Python Arithmetic Operators")
# +	Addition	x + y
x = 5
y = 3
print(x + y)
# -	Subtraction	x - y
x = 5
y = 3
print(x - y)
# *	Multiplication	x * y
x = 5
y = 3
print(x * y)
# /	Division	x / y
x = 12
y = 3
print(x / y)
# %	Modulus	x % y
x = 5
y = 2
print(x % y)
# **	Exponentiation	x ** y
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2
# //	Floor division	x // y
x = 15
y = 2
print(x // y)
#the floor division // rounds the result down to the nearest whole number

print("-*********************** Python Assignment Operators")
# =	x = 5	x = 5
x = 5
print(x)

# +=	x += 3	x = x + 3
x = 5
x += 3
print(x)

# -=	x -= 3	x = x - 3
x = 5
x -= 3
print(x)

# *=	x *= 3	x = x * 3
x = 5
x *= 3
print(x)

# /=	x /= 3	x = x / 3
x = 5
x /= 3
print(x)

# %=	x %= 3	x = x % 3
x = 5
x%=3
print(x)

# //=	x //= 3	x = x // 3
x = 5
x//=3
print(x)

# **=	x **= 3	x = x ** 3
x = 5
x **= 3
print(x)

# &=	x &= 3	x = x & 3
x = 5
print (bin(x)) # 00000000000000000000000000000101
x &= 3
print(bin(3)) #00000000000000000000000000000011
print("& : " + str(x)) #00000000000000000000000000000001

# ~	    x = ~a
x = 5
x = ~x
print("~ : " + str(x))

# |=	x |= 3	x = x | 3
x = 5
x |= 3
print("| : " + str(x))

# ^=	x ^= 3	x = x ^ 3
x = 5
x ^= 3
print("^ : " + str(x))

# >>=	x >>= 3	x = x >> 3
x = 5
x >>= 3
print(">> : " + str(x))

# <<=	x <<= 3	x = x << 3
x = 5
x <<= 3
print("<< : " + str(x))
