def depasse(M):
    """plus petit n tq 1+...+n >= M"""
    s = 0
    n = 0
    # s == 0 == n*(n+1)//2 == 1 + ... + n
    while s < M :
        # Variant : ceil(M) - s
        # Inv : s = n*(n+1)//2 == 1 + ... + n
        n= n+1
        # s == (n-1)*n // 2 == 1 + ... + (n-1)
        s = s+n
        # Inv : s == n*(n+1)//2 = 1 + ... + n
    return n
