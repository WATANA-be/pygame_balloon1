def max3(a,b,c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c

    return maximum

print(f"max3(3,2,4)={max3(3,2,4)}")
print(f"max3(5,7,9)={max3(5,7,9)}")
