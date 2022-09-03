import numpy as np
from scipy.integrate import odeint

class Simulation():
    """
    The Simulation class contains a System instance and time information required to run a simulation on it.
    In particular, it defines an odeint-like function for complex valued differential equations (self.odeintz).
    """

    def __init__(self, system, time, tstep) -> None:
        """
        Initialized all the attributes of the class.

        Parameters
        ----------
        system : System
            the system composed by the cavity field and the atom
        time : integer
            the simulation duration 
        tstep: float
            the simulation time step

        Raise:
        ------
            ValueError if the simulation duration (time) or the simulation time step (tstep)
            is negative.
            ValueError if the time step (tstep) is not sufficiently fine.

        """
        
        self.system = system

        if time < 0:
            raise ValueError("The simulation duration (time) must be positive.\n")
        if tstep < 0:
            raise ValueError("The simulation time step (tstep) must be positive.\n")

        self.time = np.arange(0,time,tstep)
        self.thr = 0.01 # threshold for the rate tstep/time
        self.W_array = []

        if tstep/time > self.thr:
            raise ValueError("The simulation time step (tstep) is too large.\n" + \
                "Consider to increase time or to decrease tstep.\n")
    
    def odeintz(self, func, z0, t, **kwargs):
        """
        An odeint-like function for complex valued differential equations.
        
        Parameters:
        -----------
        func : callable(z,t,…) 
            function with the signature func(z,t,…) that computes the derivative of z at t.
        z0 : array
            initial condition on z
        t : array
            sequence of time points for which to solve func
        **kwargs: tuple, optional
            Extra arguments to pass to function
        
        Returns:
        --------
        z : array, shape (len(t), len(y0))
            Array containing the value of z for each desired time in t,
            with the initial value z0 in the first row 
        
        """

        # Conversion of z0 to a numpy array of type np.complex128
        z0 = np.array(z0, dtype=np.complex128, ndmin=1)

        def realfunc(x, t, *args):
            z = x.view(np.complex128)
            dzdt = func(z, t, *args)
            # func might return a python list, so convert its return
            # value to an array with type np.complex128, and then return
            # a np.float64 view of that array
            return np.asarray(dzdt, dtype=np.complex128).view(np.float64)

        result = odeint(realfunc, z0.view(np.float64), t, **kwargs)
        # return a np.complex view of that array
        z = result.view(np.complex128)
        return z

    def W_numerical(self):
        """ 
        Calculate the atomic inversion function W(t).
        
        Inversion functions Wn(t) associated to a certain number of photons in the cavity (Fock states)
        are calculated solving the differential equations described in self.system.rabi_model using the
        class method self.odeintz, then they are weighted up using self.system.field.PDF (Probability
        Density Function of photon number) (PDF options: Dirac, Poisson, Bose-Einstein) and summed.
            
        Returns:
        --------
        W : array shape (len(t))
            Array containing the value of W(t) for each desired time in self.time.

        """
        W = 0 # the cavity is empty
        # we add all the contribution till the cut-off number of photons (N)
        for n in range(0,self.system.field.cut_n):                          
            res = self.odeintz(self.system.rabi_model, self.system.atom.state, self.time, args=(n,))
            # probabilities
            P_g = res[:,0].real**2 + res[:,0].imag**2
            P_e = res[:,1].real**2 + res[:,1].imag**2
            # atomic inversion function Wn(t)
            Wn = P_e - P_g
            # sum the Wn(t) with a weighted coefficients
            W = W + self.system.field.PDF(n)*Wn
        return W     # Inversion function W(t) 

    def run(self):
        """ Run a simulation on self.system """
        self.W_array = self.W_numerical()
