import numpy as np
import scipy as sc
import scipy.stats as st
from scipy.integrate import odeint

class Simulation():
    """
    The Simulation class stores
    """

    def __init__(self, System, tmax, tstep) -> None:
        """
        Initialized all the attributes of the class.

        Parameters
        ----------
        System : System
            the system composed by the cavity field and the atom
        tmax : int
            the simulation duration 
        tstep: float
            the simulation time step
        """
        
        self.System = System
        self.time = np.arange(0,tmax,tstep)
    
    def odeintz(self, func, z0, t, **kwargs):
        """An odeint-like function for complex valued differential equations.
        
        Parameters:
        -----------
            func : function with the signature func(y,t,...)
            z0 : initial condition on y (can be a vector)
            t : array of time points for which to solve func
            **kwargs: Extra arguments to pass to function
        
        Returns:
        --------
            Array containing the value of z for each desired time in t,
            with the initial value z0 in the first row
            
        Raise:
        ------
            ValueError if you pass odeint arguments not supported dy odeintz
            (Jacobian and infodict related arguments) """

        # Disallow Jacobian and infodict related arguments
        _unsupported_odeint_args = ['Dfun', 'col_deriv', 'ml', 'mu']
        bad_args = [arg for arg in kwargs if arg in _unsupported_odeint_args]
        if len(bad_args) > 0:
            raise ValueError("The odeint argument %r is not supported by "
                            "odeintz." % (bad_args[0],))

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
        
        if kwargs.get('full_output', False):
            z = result[0].view(np.complex128)
            infodict = result[1]
            return z, infodict
        else:
            z = result.view(np.complex128)
            return z

    def W(self):
        val = 0# the cavity is empty
        # we add all the contribution till the cut-off number of photons (N)
        for n in range(0,self.System.Field.cut_n):                          
            res = self.odeintz(self.System.Rabi_model, self.System.Atom.state, self.time, args=(n,))
            # probabilities
            P_g = res[:,0].real**2 + res[:,0].imag**2
            P_e = res[:,1].real**2 + res[:,1].imag**2
            # inversion function
            Wn = P_e - P_g
            val = val + self.System.Field.PDF(n)*Wn
        return val     # Inversion function W(t) 

    def run(self):
        self.W_array = self.W()