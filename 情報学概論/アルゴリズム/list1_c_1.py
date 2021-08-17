def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c

    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print("三つの整数の中央値を求める")
a = int(input("整数aの値:"))
b = int(input("整数bの値:"))
c = int(input("整数cの値:"))

print(f"中央値は{med3(a,b,c)}です。")
    