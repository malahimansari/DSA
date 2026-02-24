
# Operators in Python

# Arithmetic Operators
a = 10
b = 5
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus
print(a ** b)  # exponentiation
print(a // b)  # floor division


# Comparison Operators
c = 10
d = 5
print(c == d)  # equal to
print(c != d)  # not equal to
print(c > d)  # greater than
print(c < d)  # less than
print(c >= d)  # greater than or equal to
print(c <= d)  # less than or equal to


# Logical Operators
x = True
y = False
print(x and y)  # and
print(x or y)  # or
print(not x)  # not


# Assignment Operators
e = 10
f = 5
e += f  # e = e + f
e -= f  # e = e - f
e *= f  # e = e * f
e /= f  # e = e / f
e %= f  # e = e % f
e **= f  # e = e ** f
e //= f  # e = e // f


# Bitwise Operators
g = 10
h = 5
print(g & h)  # and
print(g | h)  # or
print(g ^ h)  # xor
print(~g)  # not
print(g << 2)  # left shift
print(g >> 2)  # right shift


# Membership Operators
i = 10
j = [1, 2, 3, 4, 5]
print(i in j)  # in
print(i not in j)  # not in


# Identity Operators
k = 10
l = 10
print(k is l)  # is
print(k is not l)  # is not



# Ternary Operators
m = 10
n = 5
print("m is greater") if m > n else print("n is greater")



# Operator Precedence and Associativity
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")
    
    
# Operator Associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)


# Walrus Operator

# The walrus operator (:=) allows you to assign values to variables as part of an expression.
num = [1, 2, 3, 4, 5]

while (n := len(num)) > 0:
    print(num.pop())