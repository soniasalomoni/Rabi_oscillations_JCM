
import numpy as np

class System():
    """
    The System class stores all the parameters that describe the system composed by the cavity field and the atom.
    In addition, the class is enriched by some interaction parameters (coupling e detuning).
    The class implement a set of complex differential equations self.rabi_model that model the time evolution
    of the system using the Jaynes-Cummings model Hamiltonian.
    """

    def __init__(self, field, atom, omega, delta) -> None:
        """
        Initialized all the attributes of the class.

        Parameters
        ----------
        field : Field
            the cavity field instance
        atom : Atom
            the atom instance
        omega: float
            the interaction coupling
        delta: float
            the interaction detuning

        Raise:
        ------
            ValueError if the interaction coefficiet (omega) is negative.

        """
        
        self.field = field
        self.atom = atom
        self.omega = omega
        self.delta = delta

        if self.omega < 0:
            raise ValueError("The interaction coefficient omega must be positive or 0.\n")


    def rabi_model(self, z, t, n):
        """
        Implement a set of complex differential equations that model the time evolution
        of the system using the Jaynes-Cummings model Hamiltonian.

        Actually, t is not used in the definition of the model, but is required in the 
        signature of the function if we want to solve it using scipy.integrate.odeint

        Parameters:
        -----------
        z : array 
            the state of the atom [Cg,Ce] 
        t : array
            array of time points for which to solve the diffeferential equations
        n : integer
            number of photons in the cavity

        Return:
        -------
        dgdt : float
            time derivative of the coefficient of the ground state
        dedt : float
            time derivative of the coefficient of the excited state

        """
        # dg/dt = func_g(g,e)
        dgdt = -1j*(self.omega/2 * np.sqrt(n) * z[1] - 1/2 * self.delta * z[0])
        # de/dt = func_e(g,e)
        dedt = -1j*(self.omega/2 * np.sqrt(n) * z[0] + 1/2 * self.delta * z[1])
        return dgdt, dedt
