def maximum_double(M):
    """Maximum de M
    Précondition : M tableau à double entrées de nombres"""
    m = M[0][0]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] > m :
                m = M[i][j]
    return m

M = [[42,1515,0,12],
     [-5,3,8,2],
     [0,-5,4242,0]]
