def f1(x):
    """-1 si x <= 1, x si -1 < x <= 1, 1 si x >=1"""
    if x < -1:
        f = -1
    elif -1 <= x < 1:
        f = x
    else :
        f = 1
    return f

def f2(x):
    """-1 si x <= 1, x si -1 < x <= 1, 1 si x >=1"""
    if x < -1:
        return -1
    elif x < 1 :
        return x
    else:
        return 1
