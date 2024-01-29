"""
    Module pour la conversion et l'affichage de la représentation binaire
    des nombres

    Module basé sur le module struct pour afficher les valeurs binaires
    correspondant à des nombres, et, inversement, traduire un code binaire
    en un nombre. Cela permet d'illustrer le binaire naturel, le format
    complément à 2 pour les entiers signés et la norme IEEE-754 pour les
    flottants.
"""

# coding: utf8
# authors : M. Gartner & T. Kovaltchouk (F. Roosevelt, Reims, France)
# date : 02/07/2021

from struct import pack, unpack, calcsize
from numbers import Number
from math import nan, inf

# Définition des couleurs pour la console
_BLACK = '\x1b[30m'
_RED = '\x1b[31m'
_GREEN = '\x1b[32m'
_YELLOW = '\x1b[33m'
_BLUE = '\x1b[34m'
_MAGENTA = '\x1b[35m'
_CYAN = '\x1b[36m'
_WHITE = '\x1b[37m'
_UNDERLINE = '\x1b[4m'
_RESET = '\x1b[0m'


def number2binary(norme:str, value:Number) -> str:
    """
    Retourne une chaine de caractère binaire correspondant à la valeur de
    l'argument value suivant la norme du format de nombre

    Parameters
    ----------
    norme : {'b', 'B', 'h', 'H', 'i', 'I', 'q', 'Q', 'e', 'f', 'd'}
        Norme en une lettre du format du nombre.
    value : Number
        Nombre à convertir.


    Returns
    -------
    str
        Chaine de caractère constituée de 0 et de 1 correspondant au nombre dans
        le format souhaité.


    Les noms de norme du format acceptés sont les suivants :

    ===== ==================================================================
    Norme                  Nombre représenté par ce format
    ===== ==================================================================
    'b'   Entier signé sur 8 bits (complément à 2) équivalent à np.int8
    'B'   Entier non-signé sur 8 bits équivalent à np.uint8
    'h'   Entier signé sur 16 bits (complément à 2) équivalent à np.int16
    'H'   Entier non-signé sur 16 bits équivalent à np.uint16
    'i'   Entier signé sur 32 bits (complément à 2) équivalent à np.int32
    'I'   Entier non-signé sur 32 bits équivalent à np.uint32
    'q'   Entier signé sur 64 bits (complément à 2) équivalent à np.int64
    'Q'   Entier non-signé sur 64 bits équivalent à np.uint64
    'e'   Flottant demi-précision équivalent à np.float16 (IEEE-754)
    'f'   Flottant simple précision équivalent à np.float32 (IEEE-754)
    'd'   Flottant double précision équivalent à np.float64 (IEEE-754)
    ===== ==================================================================

    Notes
    -----
    Le format Gros-boutisme (big-endian) est utilisé.

    See Also
    --------
    binary2number :
        Fonction inverse qui permet de retrouver un nombre à partir de sa
        représentation binaire.
    show_float : Fonction illustrant dans la console le format des flottants.
    show_int : Fonction illustrant dans la console le format des entiers.
    """
    def bytes2binary(octets):
        assert len(octets) == calcsize(norme) # respect de la taille
        bin_rep = ""
        for octet in octets:
            bin_rep += format(octet, "08b") # formatage binaire de chaque octet
        return bin_rep

    return bytes2binary(pack(">"+norme, value))

def binary2number(norme:str, repr_bin:str) -> Number:
    """
    Retourne un nombre correspondant à sa représentation binaire.

    Parameters
    ----------
    norme : {'b', 'B', 'h', 'H', 'i', 'I', 'q', 'Q', 'e', 'f', 'd'}
        Norme en une lettre du format du nombre.
    repr_bin : str
        Chaine de cacractères constituée de 0 et de 1 correspondant au nombre
        recherché. La longueur de cette chaine doit être un multiple de 8
        cohérente avec le format.


    Returns
    -------
    int or float
        Nombre résultat de la conversion : entier ou flottant suivant la valeur
        de norme.


    Les noms de norme du format acceptés sont les suivants :

    ===== ==================================================================
    Norme                  Nombre représenté par ce format
    ===== ==================================================================
    'b'   Entier signé sur 8 bits (complément à 2) équivalent à np.int8
    'B'   Entier non-signé sur 8 bits équivalent à np.uint8
    'h'   Entier signé sur 16 bits (complément à 2) équivalent à np.int16
    'H'   Entier non-signé sur 16 bits équivalent à np.uint16
    'i'   Entier signé sur 32 bits (complément à 2) équivalent à np.int32
    'I'   Entier non-signé sur 32 bits équivalent à np.uint32
    'q'   Entier signé sur 64 bits (complément à 2) équivalent à np.int64
    'Q'   Entier non-signé sur 64 bits équivalent à np.uint64
    'e'   Flottant demi-précision équivalent à np.float16 (IEEE-754)
    'f'   Flottant simple précision équivalent à np.float32 (IEEE-754)
    'd'   Flottant double précision équivalent à np.float64 (IEEE-754)
    ===== ==================================================================

    Notes
    -----
    Le format Gros-boutisme (big-endian) est utilisé.


    See Also
    --------
    number2binary :
        Fonction inverse qui permet de trouver la représentation binaire d'un
        nombre.
    """
    def binary2bytes(repr_bin):
        assert len(repr_bin)%8 == 0 # Nombre entier d'octets représentés
        mes = bytearray()
        len_mes = len(repr_bin) // 8
        assert len_mes == calcsize(norme) # respect de la taille
        for i in range(len_mes):
            mes.append( int(repr_bin[i*8:(i+1)*8], 2) ) # parcours par octet
        return bytes(mes)
    out = unpack(">"+norme, binary2bytes(repr_bin))
    assert len(out) == 1 # conversion d'un seul nombre
    return out[0]

def show_float(norme:str, value:float) -> None:
    """
    Montre sur la console, pour le flottant considéré (value) :
        - en rouge, le bit de signe ;
        - en bleu, les bits d'exposant ;
        - en vert, les bits de mantisse.

    Parameters
    ----------
    norme : {'e', 'f', 'd'}
        Norme en une lettre du format du nombre.
    value : float
        Nombre à convertir.


    Returns
    -------
    None


    Les noms de norme du format acceptés sont les suivants :

    ===== ==================================================================
    Norme                  Nombre représenté par ce format
    ===== ==================================================================
    'e'   Flottant demi-précision équivalent à np.float16 (IEEE-754)
    'f'   Flottant simple précision équivalent à np.float32 (IEEE-754)
    'd'   Flottant double précision équivalent à np.float64 (IEEE-754)
    ===== ==================================================================

    Notes
    -----
    Le format Gros-boutisme (big-endian) est utilisé

    See Also
    --------
    binary2number :
        Fonction inverse qui permet de retrouver un nombre à partir de sa
        représentation binaire.
    show_int : Fonction illustrant dans la console le format des entiers.
    """
    b = number2binary(norme, value)
    if norme == 'e':
        expo = 5 # 5 bits d'exposant (10 de mantisse)
    elif norme == 'f':
        expo = 8 # 8 bits d'exposant (23 de mantisse)
    elif norme == 'd':
        expo = 11 # 11 bits d'exposant (52 de mantisse)
    print('{3}{0}{4}{1}{5}{2}{6}'.format(b[0], b[1:(expo+1)], b[(expo+1):],
                                        _RED, _BLUE, _GREEN, _RESET))

def show_int(norme:str, value:int) -> None:
    """
    Montre sur la console, pour l'entier considéré (value), la représentation
    binaire correspondante (alternance vert/bleu pour les différents octets).

    Parameters
    ----------
    norme : {'b', 'B', 'h', 'H', 'i', 'I', 'q', 'Q'}
        Norme en une lettre du format du nombre.
    value : int
        Nombre à convertir.


    Returns
    -------
    None


    Les noms de norme du format acceptés sont les suivants :

    ===== ==================================================================
    Norme                  Nombre représenté par ce format
    ===== ==================================================================
    'b'   Entier signé sur 8 bits (complément à 2) équivalent à np.int8
    'B'   Entier non-signé sur 8 bits équivalent à np.uint8
    'h'   Entier signé sur 16 bits (complément à 2) équivalent à np.int16
    'H'   Entier non-signé sur 16 bits équivalent à np.uint16
    'i'   Entier signé sur 32 bits (complément à 2) équivalent à np.int32
    'I'   Entier non-signé sur 32 bits équivalent à np.uint32
    'q'   Entier signé sur 64 bits (complément à 2) équivalent à np.int64
    'Q'   Entier non-signé sur 64 bits équivalent à np.uint64
    ===== ==================================================================

    Notes
    -----
    Le format Gros-boutisme (big-endian) est utilisé

    See Also
    --------
    binary2number :
        Fonction inverse qui permet de retrouver un nombre à partir de sa
        représentation binaire.
    show_float : Fonction illustrant dans la console le format des flottants.
    """
    b = number2binary(norme, value)
    if len(b) == 8:
        print('{1}{0}{2}'.format(b, _GREEN, _RESET))
    else:
        for i in range(len(b)//16):
            d = i*16
            print('{2}{0}{3}{1}'.format(b[d:d+8], b[d+8:d+16],
                                        _GREEN, _BLUE), end='')
        print(_RESET)

if __name__ == "__main__":
    for nb in [1.0, 2.0, 2.2, 1.1, 0.0, -0.0, nan, inf]:
        print("Représentation binaire de ", nb)
        print("===============================")
        print("Demi-précision")
        show_float('e', nb)
        print("Simple précision")
        show_float('f', nb)
        print("Double précision")
        show_float('d', nb)
        print()

    for nb in [-1, 1, -128, 127]:
        print("Représentation binaire en complément à 2 de ", nb)
        print("=================================================")
        print("Sur 1 octet :")
        show_int('b', nb)
        print("Sur 2 octets :")
        show_int('h', nb)
        print("Sur 4 octets :")
        show_int('i', nb)
        print("Sur 8 octets :")
        show_int('q', nb)
        print()
