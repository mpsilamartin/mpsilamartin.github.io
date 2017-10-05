def est_premier_bis(n):
    """Teste si n est premier"""
    for d in range(2,n):
        # Inv : n n'a pas de diviseur dans {2,...,d-1}
        if n % d == 0 :
            return False
	# Inv : n n'a pas de diviseur dans {2,...,d}
    # Inv : au dernier tour de boucle, d = n-1, donc n n'a pas de diviseur dans {2,...,n-1}, donc n est premier
    return True
