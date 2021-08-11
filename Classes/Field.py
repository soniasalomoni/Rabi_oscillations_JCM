import numpy as np

class Field():
    """
    The Field class stores all the parameters that describe the cavity field.
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
        
        """
        
        self.avg_n = avg_n
        self.pdf_n = pdf_n
        self.cut_n = cut_n

        self.PDFs = {"Dirac" : self.Dirac,
            "Poisson" : self.Poisson,
            "BoseEinstein" : self.BoseEinstein
        }

        self.PDF = self.PDFs[pdf_n]

    def Dirac(self,n):
        if n == self.avg_n: return 1
        else: return 0

    def Poisson(self,n):
        fac = float(np.math.factorial(n)) 
        return (self.avg_n**n)/fac*np.exp(-self.avg_n)

    def BoseEinstein(self,n):
        return 1/(1+self.avg_n)*(self.avg_n/(1+self.avg_n))**n