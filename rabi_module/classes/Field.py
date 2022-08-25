import numpy as np

class Field():
    """
    The Field class stores all the parameters that describe the cavity field.
    The class implement three physically relevant distributions of photons: 
    Dirac, Poisson, BoseEinstein.
    """

    def __init__(self,avg_n,pdf_n,cut_n) -> None:
        """
        Initialized all the attributes of the class.

        Parameters
        ----------
        avg_n : integer
            average number of photons in the cavity
        pdf_n : string
            photon number probability density function
            possible values: 'Dirac', 'Poisson', 'BoseEinstein'
        cut_n : integer
            photon number cut-off
        
        Raise:
        ------
            ValueError if the average number of photons (avg_n) or the cut-off
            number of photons (cut_n) is a negative integer.
            ValueError if the average number of photons is greater or equal to the
            cut-off number of photons (avg_n >= cut_n).
            ValueError if the cut-off number of photons is not sufficiently big
            to neglect the tail of the PDF of photons.
        
        """
        
        # initialize all the class attributes
        self.avg_n = avg_n
        self.pdf_n = pdf_n
        self.cut_n = cut_n
        self.thr_n = 0.001

        # check the physical meaning of the class attributes
        if self.avg_n < 0:
            raise ValueError("The average number of photons (avg_n) must be a positive integer.\n")

        if self.cut_n < 0:
            raise ValueError("The cut-off number of photons (cut_n) must be a positive integer.\n")

        if self.avg_n >= self.cut_n:
            raise ValueError("The average number of photons (avg_n) must be smaller " + \
                "then the cut-off number of photons (cut_n).\n")

        self.PDFs = {"Dirac" : self.Dirac,
            "Poisson" : self.Poisson,
            "BoseEinstein" : self.BoseEinstein
        }

        self.PDF = self.PDFs[pdf_n]

        if self.PDF(self.cut_n) > self.thr_n:
            raise ValueError("The cut-off number of photons (cut_n) is too small.\n" + \
                "Consider to increase cut_n or to decrease avg_n.\n")

    # define the allowed PDF (Probability Density Function) of photons

    def Dirac(self,n):
        """
        Model a Dirac distribution of photons.

        The average number of photons is given by self.avg_n.
        With this distribution of photons the classic behavior is found.

        Parameters:
        -----------
        n : integer
            number of photons in the cavity

        Returns:
        --------
        |Cn|^2 : float [0,1]
            Probability to find n number of photons in the cavity

        """
        if n == self.avg_n: return 1
        else: return 0

    def Poisson(self,n):
        """
        Model a Poisson distribution of photons.

        The average number of photons is given by self.avg_n.
        With this distribution of photons the field is in a coherent state.

        Parameters:
        -----------
        n : integer
            number of photons in the cavity

        Returns:
        --------
        |Cn|^2 : float [0,1]
            Probability to find n number of photons in the cavity

        """
        fac = np.math.factorial(n)
        return (self.avg_n**n)/fac*np.exp(-self.avg_n)

    def BoseEinstein(self,n):
        """
        Model a Bose-Einstein distribution of photons.

        The average number of photons is given by self.avg_n.
        With this distribution of photons the cavity is thermalized (fixed temperature).

        Parameters:
        -----------
        n : integer
            number of photons in the cavity

        Returns:
        --------
        |Cn|^2 : float [0,1]
            Probability to find n number of photons in the cavity

        """
        return 1/(1+self.avg_n)*(self.avg_n/(1+self.avg_n))**n