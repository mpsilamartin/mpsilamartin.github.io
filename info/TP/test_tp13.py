from prog import *
import pytest
import numpy as np

## Question 1 

def test_q1_1():
    A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
    trans_ligne(A,0,1,3.)
    assert np.array_equal(A,np.array([[13., 17., 21.],[ 4.,  5.,  6.], [ 7.,  8.,  9.]]))

def test_q1_2():
    A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
    trans_ligne(A,2,0,-2.)
    assert np.array_equal(A,np.array([[1., 2., 3.], [4., 5., 6.], [5., 4., 3.]]))

## Question 2

def test_q2_1():
    A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
    trans_colonne(A,0,1,3.)
    assert np.array_equal(A,np.array([[  1.,  -1.,   3.], [  4.,  -7.,   6.], [  7., -13.,   9.]]))

def test_q2_2():
    A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
    trans_colonne(A,2,0,-2.)
    assert np.array_equal(A,np.array([[ 7.,  2.,  3.], [16.,  5.,  6.], [25.,  8.,  9.]]))

## Question 3 

def test_q3_1L():
    A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
    I, _ = LU(A)
    assert np.array_equal(I, np.array([[ 1.,  0.,  0.], [ 4.,  1.,  0.], [ 7.,  2.,  1.]]))

def test_q3_1U():
    A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
    _, B = LU(A)
    assert np.array_equal(B, np.array([[ 1.,  2.,  3.], [ 0., -3., -6.], [ 0.,  0.,  0.]]))

def test_q3_2L():
    A = np.array([[9., 2., 9.], [5., 5., 8.], [6., 3., 0.]])
    I, _ = LU(A)
    assert np.allclose(I, np.array([[ 1.,  0.,  0.], [ 0.55555556,  1. ,  0. ], [ 0.66666667,  0.42857143,  1. ]]))

def test_q3_2U():
    A = np.array([[9., 2., 9.], [5., 5., 8.], [6., 3., 0.]])
    _, B = LU(A)
    assert np.allclose(B, np.array([[ 9.,  2. ,  9. ],[ 0. ,  3.88888889,  3.  ],[ 0. ,  0.  , -7.28571429]]))

## Question 4 

def test_q4_1():
    U = np.array([[1.,2.,3.],[0.,4.,5.],[0.,0.,6.]])
    B = np.array([[24., 2.],[24.,4.],[24.,6.]])
    X = resolution_sup(U,B)
    assert np.array_equal(X, np.array([[ 10.  ,  -0.5 ],  [  1.  ,  -0.25], [  4.  ,   1.  ]]))

def test_q4_2():
    U = np.array([[1.,2.,3.],[0.,4.,5.],[0.,0.,6.]])
    B = np.array([[5.],[7.],[-1.]])
    X = resolution_sup(U,B)
    assert np.allclose(X, np.array([[ 1.58333333], [ 1.95833333], [-0.16666667]]))


## Question 5 

def test_q5_1():
    L = np.array([[1.,0,0],[2.,3.,0],[4.,5.,6.]])
    B = np.array([[1., 2.],[5.,4.],[15.,8.]])
    X = resolution_inf(L,B)
    assert np.array_equal(X, np.array([[ 1.,  2.],[ 1.,  0.], [ 1.,  0.]]))

def test_q5_2():
    L = np.array([[1.,0,0],[2.,3.,0],[4.,5.,6.]])
    B = np.array([[4.],[7.],[-1.]])
    X = resolution_inf(L,B)
    assert np.allclose(X, np.array([[ 4. ], [-0.33333333], [-2.55555556]]))

