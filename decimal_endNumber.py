Write a function that returns only the decimal part of the given number.

You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.

-------------------------------------
Solution


def get_decimal(n):
    if n>0:
        b=n-int(n)
    elif n == 0:
        b=0
    else:
        b=-(n-int(n))
    print (b)



get_decimal(10)
get_decimal(1.2)
