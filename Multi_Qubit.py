import qutip as qt
from qutip.qip.operations import hadamard_transform

psi = qt.basis(2,0) # PSI
phi = qt.basis(2,1) # PHI

Multi = qt.tensor(psi, phi)
print(Multi)

H = hadamard_transform()
I = qt.qeye(2)

print(qt.tensor(H, I))