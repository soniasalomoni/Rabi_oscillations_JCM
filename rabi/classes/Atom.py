
class Atom():
    """
    The Atom class stores the parameters that describe the state of the atom in the cavity.
    By defalut,  the Atom is initialized in the ground state.
    """

    def __init__(self,Cg=1,Ce=0) -> None:
        """
        Initialized all the attributes of the class.

        Parameters
        ----------
        Cg : float
            ground state |g> coefficient
        Ce : float
            excited state |e> coefficient
        
        Raise:
        ------
            ValueError if the ground state (Cg) or the excited state (Ce)
            coefficients are negative or greater than 1.
            ValueError if the ground state (Cg) and excited state (Ce)
            coefficients are not normalized.
        
        """
        
        self.Cg = Cg
        self.Ce = Ce
        self.thr = 0.01

        if self.Cg < 0 or self.Cg > 1:
            raise ValueError("The initial ground state coefficient (Cg) must be within [0,1].\n")

        if self.Ce < 0 or self.Ce > 1:
            raise ValueError("The initial excited state coefficient (Ce) must be within [0,1].\n")

        if abs(self.Cg**2 + self.Ce**2 - 1) >= self.thr:
            raise ValueError("the ground state (Cg) and excited state (Ce) coefficients are not normalized.\n")

        # redundant but convenient information
        self.state = [Cg,Ce]