r1 = 1+1.2e-16
r2=1
a,b,c = 1, -(r1+r2), r1*r2

D = b**2-4*a*c

f = lambda x : a*x**2 + b*x + c

