import matplotlib.pyplot as plt
x = [1, 30, 400, 2000]
y = [2, 1, 4, 2]
plt.clf()
plt.plot(x,y,'or--',label='$\\frac{\\arccos(\\pi t)}{\\alpha^2}$',linewidth=3)
plt.legend()
plt.xlabel('$\\beta$')
plt.ylabel('$\\Gamma$')
# plt.xlim([-0.5+min(x),0.5+max(x)])
# plt.ylim([-0.5+min(y),0.5+max(y)])
plt.axis([-0.5+min(x),0.5+max(x),-1+min(y),0.5+max(y)])
plt.xscale('log')
plt.savefig("images/fig/ex_base_02.png")