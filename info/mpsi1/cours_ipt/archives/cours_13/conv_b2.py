def conv_b2(p):
    """Convertit p en base 2"""
    x = p
    s = ""
    while x>1:
        s = str(x%2) + s
        x = x // 2
    return str(x) + s
