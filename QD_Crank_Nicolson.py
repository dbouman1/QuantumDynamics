import scipy.sparse as sparse
import scipy.sparse.linalg as linalg
import matplotlib.pyplot as plt
import numpy as np

c1 = 5.j        # i*hbar*dt/(4*m*dx^2)
c2 = 1.j        # i*dt/(2*hbar)
n = 100         # number of points
dx = 1.0/n

# set a potential
v = 1.0*np.zeros(n)

## numerically solve for the matrix equation A*psi(t+dt) = B*psi(t) where A and B are tridiagonal matrices ##

A = sparse.diags(1.+2.*c1+c2*v, 0) - c1*sparse.eye(n,n,1) - c1*sparse.eye(n,n,-1)
B = sparse.diags(1.-2.*c1-c2*v, 0) + c1*sparse.eye(n,n,1) + c1*sparse.eye(n,n,-1)

# generate x-coordinates and initial wave-function
mean = 0.5
sigma = 0.05
x = np.linspace(0,1,n)
psi = np.exp(-(x-mean)**2/(2*sigma**2)) * np.exp(20.j*x)    # phase factor guessed
psi /= np.sqrt(sum(abs(psi)**2*dx)) # normalize the wave function

# start loop
plt.figure()
for i in range(10):
    [psi, garbage] = linalg.bicgstab(A, B*psi)
    plt.plot(x, np.abs(psi)**2)

#####
print "norm at the end: "
print sum(abs(psi)**2)*dx
plt.show()