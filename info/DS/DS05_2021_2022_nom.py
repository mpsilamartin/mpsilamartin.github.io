#DS5 MPSI 2021-2022


def Lu(alpha):
    """u_n, u_0 = alpha"""
    x = 0
    M=[]
    n=500+(-1)**alpha*2*alpha%97
    a=137
    c=187
    m=2**8
    maxi=m-3*alpha%13
    for i in range(n):
        x = (a * x+c) % m
    return M


def u(alpha,n):
    """u_n, u_0 = alpha"""
    x = alpha
    for i in range(n):
        x = (15091 * x) % 64007
    if x%26>=4:
        return x%26
    else:
        return (x+6)%26

mess="pour etre quelque chose, pour être soi-meme et toujours un, il faut agir comme on parle ; il faut etre toujours decide sur le parti que l'on doit prendre, le prendre hautement, et le suivre toujours"
alphabet="abcdefghijklmnopqrstuvwxyz"
code=""


def charger_texte_crypter(alpha):
    with open('texte_mystere_'+str(alpha)+'.txt','r') as f:
        code=f.read()
    return code

