import numpy as np
from interface import Qubit
from abc import ABCMeta, abstractmethod
from interface import Qubit, QuantumDevice
import qutip as qt

KET_0 = np.array([[1] , [0]], dtype= 'complex')
X = np.array([[0,1] , [1, 0]], dtype= 'complex') / np.sqrt(2)
H = np.array([[1,1], [1,-1]], dtype= 'complex') / np.sqrt(2)

class SimulatedQubit(Qubit):
    def __init__(self):
        self.reset()
    
    def h(self):
        self.state = H @ self.state

    def x(self):
        self.state  = X @ self.state

    def measure(self) -> bool:
        pr0 = np.abs(self.state[0, 0]) ** 2
        sample = np.random.random() <= pr0
        return bool(0 if sample else 1)
    
    def reset(self):
        self.state = KET_0.copy()

class Simulator(QuantumDevice):
    capacity: int
    available_qubits: list[SimulatedQubit]
    register_state: qt.Qobj
    
    def __init__(self, capacity = 3):
        self.capacity = capacity
        self.available_qubits = [SimulatedQubit(self, idx) for idx in range(capacity)]
        self.register_state = qt.tensor(*[qt.basis(2, 0) for _ in range(capacity)])

    def allocate_qubit(self) -> SimulatedQubit:
        if self.available_qubits:
            return self.available_qubits.pop()

    def deallocate_qubit(self, qubit: SimulateQubit):
        self.available_qubits.append(qubit)


