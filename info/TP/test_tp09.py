from prog import *
import pytest

## Partie I :  Calcul des termes successifs d'une suite recurrente

vu0 = pytest.mark.parametrize("u0, un",[
        (0, 0),
        (1.5, 1.5),
        (-2, -2),
])

@vu0
def test_valeur_u0(u0,un):
    assert valeur_u(0,u0) == un

vun = pytest.mark.parametrize("n, u0, un",[
        (10, 2, 1.0017707652224817),
        (100, 0, 1),
        (37, -1, 1.000000000013197),
])

@vun
def test_valeur_un(n,u0,un):
    assert abs(valeur_u(n,u0) - un) < 10**(-52)

hexadecimale = pytest.mark.parametrize("s, n", [
        ("0", 0),
        ("b", 11),
        ("10", 16),
        ("a2b3", 41651),
])

appu = pytest.mark.parametrize("eps, u0, n",[
        (10**-2, 0, 7),
        (10**-40, 1, 0),
        (10**-10, -2, 36),
])

@appu
def test_approche_u(eps,u0,n):
    assert approche_u(eps,u0) == n

## Partie II : records d'un tableau

rec = pytest.mark.parametrize("t, k, boo",[
        ([0], 0, True),
        ([0,1,2,3,4], 2, True),
        ([1,0,2,3], 1, False),
	([1,4,-1,0,2,5],4,False),
])

@rec
def test_record(t,k,boo):
    assert record(t,k) == boo

nbrec = pytest.mark.parametrize("t, n",[
	([],0),
        ([0], 1),
        ([0,1,2,3,4], 5),
        ([1,0,2,3], 3),
	([1,4,-1,0,2,5],3),
])

@nbrec
def test_nb_records(t,n):
    assert nb_records(t) == n

## Partie III : palindromes

epal = pytest.mark.parametrize("s, boo",[
        ('', True),
        ('esoperesteicietserepose', True),
        ('je ne suis pas un palindrome', False),
	('aabb', False),
])

@epal
def test_est_pal(s,boo):
    assert est_pal(s) == boo

mpal = pytest.mark.parametrize("s, k, p",[
        ('esoperesteicietserepose', 0, 'esoperesteicietserepose'),
        ('bumeuzo', 3, 'e'),
	('123324', 1, '2332'),
])

@mpal
def test_max_pal(s,k,p):
    assert max_pal(s) == (p,k)

mpalvide = pytest.mark.parametrize("s",[
        ('je ne suis pas un palindrome'),
	('gabubuga'),
])

@mpalvide
def test_max_pal_vide(s):
    (p,k) = max_pal(s)
    assert p == ''

## Partie IV : resume d'un fichier

def test_resume_vide():
    f = open('exemple1.txt','w')
    f.close()
    assert resume('exemple1.txt') == (1,0,0)    

def test_resume():
    f = open('exemple2.txt','w')
    f.write('\tDevise Shadock :\nPourquoi faire simple quand on peut faire compliqué ?')
    f.close()
    assert resume('exemple2.txt') == (2,12,71)

## Partie V : Crible d'Eratosthene

crib = pytest.mark.parametrize("p, li",[
        (0,[]),
        (1,[]),
        (2,[2,3]),
	(3,[2,3,5,7]),
	(10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
])

@crib
def test_crible(p,li):
    assert crible(p) == li

## Partie VI : une petite enigme

def test_enigme1():
    assert enigme() > 3

def test_enigme2():
    assert enigme() < 10**(20)

def test_enigme3():
    assert ((enigme() * 94512) % 431479) == 101658
