
import numpy as np

class System():
    """
    The Atom class stores all the parameters that describe the system composed by the cavity field and the atom.
    Also interaction parameters are stored.
    """

    def __init__(self, Field, Atom, Omega, Delta) -> None:
        """
        Initialized all the attributes of the class.

        Parameters
        ----------
        Field : Field
            the cavity field instance
        Atom : Atom
            the atom instance
        Omega: float
            the interaction coupling
        Delta: float
            the interaction detuning
        """
        
        self.Field = Field
        self.Atom = Atom
        self.Omega = Omega
        self.Delta = Delta


    def Rabi_model(self,state,time,n):
        dgdt = -1j*(self.Omega/2 * np.sqrt(n) * state[1] - 1/2 * self.Delta * state[0])
        dedt = -1j*(self.Omega/2 * np.sqrt(n) * state[0] + 1/2 * self.Delta * state[1])
        return dgdt, dedt
