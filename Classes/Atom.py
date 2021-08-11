

class Atom():
    """
    The Atom class stores all the parameters that describe the state of the atom.
    """

    def __init__(self,Cg,Ce) -> None:
        """
        Initialized all the attributes of the class.

        Parameters
        ----------
        Cg : float
            ground state |g> coefficient at time t ...
        Ce : float
            excited state |e> coefficient at time t ...
        
        """
        
        self.Cg = Cg
        self.Ce = Ce
        self.state = [Cg,Ce]