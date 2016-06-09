from prog import *
import pytest
from math import log


## Q1 : calcul de f

vf = pytest.mark.parametrize("x, fx",[
        (0.1, -0.8090169943749473),
        (0.32, -0.3090169943749511),
        (0.6, -0.5),
        (0.8, 0.6290169943749433)
])

@vf

def test_Q1(x,fx):
    assert abs(f(x)-fx) <= 10**(-13)

## Q4 : rectangles à gauche

mrg = pytest.mark.parametrize("g, a, b, N, I",[
        (f, 0, 1, 100, -0.09279999999999966),
	(f, 0, 0.1, 3, 0.05215340476970683),
	(log, 1, 2, 10, 0.3512205777177568)
])

@mrg
def test_Q4(g,a,b,N,I):
    assert abs(Rg(g,a,b,N)-I) <= 10**(-13)

## Q5 : rectangles à droite

mrd = pytest.mark.parametrize("g, a, b, N, I",[
        (f, 0, 1, 100, -0.09279999999999962),
	(f, 0, 0.1, 3, -0.008147161709458091),
	(log, 1, 2, 10, 0.42053529577375126)
])

@mrd
def test_Q5(g,a,b,N,I):
    assert abs(Rd(g,a,b,N)-I) <= 10**(-13)

## Q6 : Trapèzes

mT = pytest.mark.parametrize("g, a, b, N, I",[
        (f, 0, 1, 100, -0.09279999999999963),
	(f, 0, 0.1, 3, 0.022003121530124372),
	(log, 1, 2, 10, 0.385877936745754)
])

@mT
def test_Q6(g,a,b,N,I):
    assert abs(T(g,a,b,N)-I) <= 10**(-13)

## Q7 : Simpson

mS = pytest.mark.parametrize("g, a, b, N, I",[
        (f, 0, 1, 100, -0.08666666666666666),
	(f, 0, 0.1, 3, 0.023391317221542536),
	(log, 1, 2, 10, 0.3862943005943565),
])

@mS
def test_Q7(g,a,b,N,I):
    assert abs(S(g,a,b,N)-I) <= 10**(-13)

## Q8 : psi

vpsi = pytest.mark.parametrize("r, i, x, p",[
        (0,0,0.2,1),
	(0,0,0.7,-1),
	(1,0,0.2,1.4142135623730951),
	(1,0,0.4,-1.4142135623730951),
	(1,0,0.7,0),
	(7,15,0.1203125,11.313708498984761),
	(7,15,0.121875,-11.313708498984761),
	(7,15,0.5,0)
])

@vpsi
def test_Q8(r,i,x,p):
    assert abs(psi(r,i,x)-p) <= 10**(-13)

# Q11 : alpha

va = pytest.mark.parametrize("r, i, a",[
        (0,0,0.3334166666666666),
	(1,0,-0.17674723251408753),
	(1,1,-0.05860147449083521),
	(7,15,0.0004249306840320247),
	(7,42,-0.023819220498802612),
])

@va
def test_Q11(r,i,a):
    assert abs(alpha(r,i)-a) <= 10**(-13)

# Q12 : fchap

vfchap = pytest.mark.parametrize("a, t, N, fc",[
        ([[1],3],0.3,0,4),
	([[2],-1],0.7,0,-3),
	([[2],-1],0.7,0,-3),
	([[2],[0,1],[4,-1,3,3],-1],0.8,2,1.585786437626905),
	([[1],[2,-1],[0,-1,7,-3],-2],0.3,2,-5.82842712474619),
])

@vfchap
def test_Q12(a,t,N,fc):
    assert abs(fchap(a,t,N)-fc) <= 10**(-13)
