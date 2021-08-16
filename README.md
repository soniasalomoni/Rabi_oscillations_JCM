<p>
<img src="https://img.icons8.com/ios/250/000000/bookmark-ribbon.png" width="10%">
</p>


# The Jaynes-Cummings model and Rabi Oscillations

The [**Jaynes-Cummings model**](https://en.wikipedia.org/wiki/Jaynes%E2%80%93Cummings_model) (JCM) is a soluble fully quantum mechanical model of an atom in a field. It was first used in 1963 to examine the classical aspects of spontaneous emission and to reveal the existence of [**Rabi oscillations**](https://en.wikipedia.org/wiki/Rabi_cycle) in atomic excitation probabilities for fields with sharply defined energy (or photon number).
For fields having a statistical distribution of photon numbers the oscillations collapse to an expected steady value. In 1980 it was discovered that with appropriate initial conditions (e.g. a near-classical field), the Rabi oscillations would eventually revive, only to collapse and revive repeatedly in a complicated pattern. The existence of these revivals, present in the analytic solutions of the JCM, provided direct evidence for discreteness of field excitation (photons) and hence for the truly quantum nature of radiation.
The relative simplicity of the JCM and the ease with which it can be extended through analytic expressions or numerical computation continues to motivate attention. Here is presented a brief overview of this theory; if you are interested in learning more about the topic, I recommend reading these papers:

- Bruce W. Shore and Peter L. Knight. **"The Jaynes-Cummings model"**. In: *Journal of Modern Optics*, vol. 40, no. 7, 1195-1238 (1993). DOI: 10.1080/09500349314551321. URL:  [https://www.researchgate.net/publication/243401964_The_Jaynes-Cummings_Model](https://www.researchgate.net/publication/243401964_The_Jaynes-Cummings_Model)
- Fabio D. Bonani. **"The Jaynes-Cummings model"**. (2020). URL:
[https://www.ifsc.usp.br/~strontium/Teaching/Material2020-1 SFI5814 Atomicamolecular/Fabio - Monograph - Jaynes-Cummings model.pdf](https://www.ifsc.usp.br/~strontium/Teaching/Material2020-1%20SFI5814%20Atomicamolecular/Fabio%20-%20Monograph%20-%20Jaynes-Cummings%20model.pdf)  

<img src="https://img.icons8.com/ios/50/000000/notion.png" width="30px" height="30px"> Check this [Notion page](https://radical-ketch-a32.notion.site/The-Jaynes-Cummings-model-56651cd955934b1dae5f9bb668545a4f)  

**INDEX**

> [**Mathematical formulation**](#Mathematical-formulation)  
> - [The Jaynes-Cummings Hamiltonian](#The-Jaynes-Cummings-Hamiltonian)  
> - [The Jaynes-Cummings ladder](#The-Jaynes-Cummings-ladder)  
> - [Rabi oscillations](#Rabi-oscillations)  
> - [Initial conditions: mixtures](#Initial-conditions-mixtures)  
>  
> [**Repository Structure**](#Code-Structure)
> - [Classes](#Classes)
> - [Utilities](#Utilities)
> - [Testing](#Testing)
> - [Output](#Output)
> - [Jobs](#Jobs)
>
> [**Usage**](#Usage)

## **Mathematical formulation**

### The Jaynes-Cummings Hamiltonian

The Hamiltonian that describes the full system consists of the *free field Hamiltonian* <img src="https://latex.codecogs.com/svg.image?\bg_white&space;\hat{H}_{f}" title="\inline \hat{H}_{f}"/>, the *atomic excitation Hamiltonian* <img src="https://latex.codecogs.com/svg.image?\bg_white&space;\hat{H}_{e}" title="\inline\hat{H}_{e}" />, and the *Jaynes–Cummings interaction Hamiltonian* <img src="https://latex.codecogs.com/svg.image?\bg_white&space;\hat{H}_{int}" title="\inline\hat{H}_{int}" />:

<p  align="center">
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;\hat{H}_{JC}=&space;&space;\hat{H}_f&space;&plus;&space;\hat{H}_e&space;&plus;&space;\hat{H}_{int}&space;=&space;\hbar&space;\omega_0&space;(\hat{a}^\dagger&space;\hat{a})&space;&plus;\hbar&space;\omega_e&space;(\hat{b}^\dagger&space;\hat{b})&space;&plus;\hbar&space;\Omega&space;(\hat{a}^\dagger&space;\hat{b}&space;&plus;&space;\hat{a}\hat{b}^\dagger)" title="\hat{H}_{JC}= \hat{H}_f + \hat{H}_e + \hat{H}_{int} = \hbar \omega_0 (\hat{a}^\dagger \hat{a}) +\hbar \omega_e (\hat{b}^\dagger \hat{b}) +\hbar \Omega (\hat{a}^\dagger \hat{b} + \hat{a}\hat{b}^\dagger)" />
 <p/>

- **free field Hamiltonian:** <img src="https://latex.codecogs.com/svg.image?\hat{H}_f&space;=&space;\hbar&space;\omega_0&space;(\hat{a}^\dagger&space;\hat{a})" title="\hat{H}_f = \hbar \omega_0 (\hat{a}^\dagger \hat{a})" /> `// Quantization of the free electromagnetic field`  
The operator <img src="https://latex.codecogs.com/svg.image?\hat{a}^\dagger&space;\hat{a}" title="\inline \hat{a}^\dagger \hat{a}" /> is the *number operator* <img src="https://latex.codecogs.com/svg.image?\hat{n}" title="\inline \hat{n}" /> and its expectation value is a positive integer and represents the number of quantized oscillations present in the system. The operators <img src="https://latex.codecogs.com/svg.image?\hat{a}^\dagger" title="\inline \hat{a}^\dagger" /> and <img src="https://latex.codecogs.com/svg.image?\hat{a}" title="\inline \hat{a}" /> are the *bosonic creation and annihilation operators* and <img src="https://latex.codecogs.com/svg.image?\omega_0" title="\inline \omega_0" /> is the *angular frequency* of the mode.
- **excitation Hamiltonian:** <img src="https://latex.codecogs.com/svg.image?\hat{H}_e&space;=&space;\hbar&space;\omega_e&space;(\hat{b}^\dagger&space;\hat{b})" title="\inline \hat{H}_e = \hbar \omega_e (\hat{b}^\dagger \hat{b})" />  `// Quantization of matter`   
the operator <img src="https://latex.codecogs.com/svg.image?\hat{b}^\dagger" title="\inline \hat{b}^\dagger" /> produces a transition from the atomic ground state <img src="https://latex.codecogs.com/svg.image?|g\rangle" title="\inline \ket{g}" /> to the excited state <img src="https://latex.codecogs.com/svg.image?|e\rangle" title="\inline \ket{e}" />, while the operator <img src="https://latex.codecogs.com/svg.image?\hat{b}" title="\inline \hat{b}" /> produces a de-excitation of the atom, making a transition from the state <img src="https://latex.codecogs.com/svg.image?|e\rangle" title="\inline \ket{e}" /> to the state <img src="https://latex.codecogs.com/svg.image?|g\rangle" title="\inline \ket{g}" />; <img src="https://latex.codecogs.com/svg.image?\omega_e" title="\inline \omega_e" /> is the *transition frequency* between the two energy levels of the atom.
The *raising and lowering operators* <img src="https://latex.codecogs.com/svg.image?\hat{b}^\dagger" title="\inline \hat{b}^\dagger" /> and <img src="https://latex.codecogs.com/svg.image?\hat{b}" title="\inline \hat{b}" /> behave respectively as a sort of *creation and annihilation operators* for electronic excitation.
- **JCM interaction Hamiltonian:**  <img src="https://latex.codecogs.com/svg.image?\hat{H}_{int}&space;=&space;\hbar&space;\Omega&space;(\hat{a}^\dagger&space;\hat{b}&space;&plus;&space;\hat{a}\hat{b}^\dagger)" title="\inline \hat{H}_{int} = \hbar \Omega (\hat{a}^\dagger \hat{b} + \hat{a}\hat{b}^\dagger)" /> `// Quantization of interaction`  
The construction of the JCM Hamiltonian is such that each photon creation accompanies an atomic de-excitation, and each photon annihilation accompanies atomic excitation. The conservation of the number of excitation is reached using the [**rotating wave approximation**](https://en.wikipedia.org/wiki/Rotating_wave_approximation) (RWA). <img src="https://latex.codecogs.com/svg.image?\Omega" title="\Omega" /> has the dimensions of the inverse of a time and is called the *vacuum* (or single-photon) *Rabi frequency*. This quantity can be seen as a measure of the coupling between light and matter.

The *field frequency* <img src="https://latex.codecogs.com/svg.image?\omega_0" title="\inline \omega_0" />, the *atomic transition frequency* <img src="https://latex.codecogs.com/svg.image?\omega_e" title="\inline \omega_e" />, and the (*vacuum*) *Rabi frequency* <img src="https://latex.codecogs.com/svg.image?\Omega" title="\Omega" />, appear as arbitrary parameters in the theory, although in applications they are fixed by physical considerations (e.g. the *cavity volume* <img src="https://latex.codecogs.com/svg.image?V" title="\inline V" /> and the *atomic transition moment* <img src="https://latex.codecogs.com/svg.image?d" title="\inline d" />, as in the expression <img src="https://latex.codecogs.com/svg.image?\Omega^2&space;=&space;d^2\omega_0/\hbar&space;\varepsilon_0&space;V" title="\Omega^2 = d^2\omega_0/\hbar \varepsilon_0 V" />).  
Missing from the JCM Hamiltonian are such effects as cavity loss, multiple cavity modes, atomic sublevel degeneracy and atomic polarizability (leading to dynamic Stark shifts).

### The Jaynes-Cummings ladder

The interaction Hamiltonian can only cause transitions of type <img src="https://latex.codecogs.com/svg.image?|e,n-1\rangle&space;\leftrightarrow&space;|g,n\rangle"/>, where these product states are referred to be as the *bare states* of the Jaynes-Cummings model. For a fixed <img src="https://latex.codecogs.com/svg.image?n"/>, the dynamics of the system are confined to the two-dimensional space of product states <img src="https://latex.codecogs.com/svg.image?\{|g,n\rangle,|e,n-1\rangle\}"/>.

<p  align="center">
<img src="./Images/image_1.png" width="80%" height="80%">
</p>

The Hamiltonian can be written as:

<p  align="center">
<img src="https://latex.codecogs.com/svg.image?\hat{H}_{JC}&space;=&space;\begin{pmatrix}&space;&space;&space;&space;&space;&space;&space;&space;E_1&space;&&space;W_{12}\\&space;&space;&space;&space;&space;&space;&space;&space;W_{21}&space;&&space;E_2&space;&space;&space;&space;\end{pmatrix}&space;&space;&space;&space;=\hbar&space;&space;&space;&space;\begin{pmatrix}&space;&space;&space;&space;&space;&space;&space;&space;n\omega_0-\frac{1}{2}\Delta&space;&&space;\frac{1}{2}\Omega\sqrt{n}\\&space;&space;&space;&space;&space;&space;&space;&space;\frac{1}{2}\Omega\sqrt{n}&space;&&space;n\omega_0&plus;\frac{1}{2}\Delta&space;&space;&space;&space;\end{pmatrix}" title="\hat{H}_{JC} = \begin{pmatrix} E_1 & W_{12}\\ W_{21} & E_2 \end{pmatrix} =\hbar \begin{pmatrix} n\omega_0-\frac{1}{2}\Delta & \frac{1}{2}\Omega\sqrt{n}\\ \frac{1}{2}\Omega\sqrt{n} & n\omega_0+\frac{1}{2}\Delta \end{pmatrix}" />
</p>

where <img src="https://latex.codecogs.com/svg.image?E_1"/> corresponds to the energy of the bare state <img src="https://latex.codecogs.com/svg.image?|g,n\rangle"/>, while <img src="https://latex.codecogs.com/svg.image?E_2"/> indicates the energy of the state <img src="https://latex.codecogs.com/svg.image?|e,n-1\rangle"/>: it is important to note that the two bare states differ for an *energy gap* equal to <img src="https://latex.codecogs.com/svg.image?\hbar\Delta"/>, with <img src="https://latex.codecogs.com/svg.image?\Delta&space;=&space;\omega_e-\omega_0"/>. Finally, the off-diagonal elements <img src="https://latex.codecogs.com/svg.image?W_{12}"/> and <img src="https://latex.codecogs.com/svg.image?W_{21}"/> model the perturbation given by the interaction terms.  
Due to the presence of the interaction terms, the Jaynes-Cummings Hamiltonian does not have as eigenstates the bare states, but a linear combination of them. By performing the diagonalization of the matrix, it is possible to calculate the energy eigenvalues relating to the new mixed states, called *dressed states*.  
In a similar fashion, also the energies allowed to the system change; in particular, when the system is close to the resonance, that is <img src="https://latex.codecogs.com/svg.image?\omega_0\simeq\omega_e"/>, a splitting of the energy levels occurs.

<p  align="center">
 <img src="https://latex.codecogs.com/svg.image?E_{\pm,n}&space;=&space;n\hbar\omega_0\pm\frac{1}{2}\hbar\Omega_{n}\qquad\Omega_{n}&space;=&space;\sqrt{\Delta^2+\Omega^2n}"/>  <br>
 <img src="https://latex.codecogs.com/svg.image?|\pm,n\rangle&space;=&space;|g,n\rangle\sqrt{\frac{\Omega_{n}\mp\Delta}{2\Omega_{n}}}\pm|e,n-1\rangle\sqrt{\frac{\Omega_{n}\pm\Delta}{2\Omega_{n}}}"/>
<p/>

The new polaritonic states <img src="https://latex.codecogs.com/svg.image?|\pm,n\rangle"/> possess hybrid characteristics, being a combination of photons and electronic excitations. Moreover, in these mixed states, photons and the exciton are said to be *entangled*, since they cannot be written as a simple product of the bases of separate systems.

<p  align="center">
 <img src="./Images/image_2.png" width="60%" height="60%">
</p>

First, we rewrite the Hamiltonian <img src="https://latex.codecogs.com/svg.image?\hat{H}_{JC}"/> in a new "reference system", in order to set the energy of the ground state equal to 0 (in practice it is subtracted a term proportional to the identity matrix, which therefore does not modify the dynamics of the system):

<p  align="center">
 <img src="https://latex.codecogs.com/svg.image?\hat{H}_{JC}&space;=&space;\begin{pmatrix}0&space;&&space;\frac{1}{2}\Omega\sqrt{n}\\\frac{1}{2}\Omega\sqrt{n}&space;&&space;\Delta\end{pmatrix}&space;\hbar" />
<p/>


We can notice that the curves relating to the energy of the separate system ( <img src="https://latex.codecogs.com/svg.image?\Omega&space;=&space;0"/> ) intersect for <img src="https://latex.codecogs.com/svg.image?\Delta&space;=&space;0"/>, e.g. under conditions of perfect resonance. When the two systems are coupled ( <img src="https://latex.codecogs.com/svg.image?\Omega&space;\neq&space;0 "/> ), however, this degeneration is eliminated, in fact the curves relating to the dressed states are hyperbolas, whose asymptotes are the lines <img src="https://latex.codecogs.com/svg.image?E_g"/> and <img src="https://latex.codecogs.com/svg.image?E_e"/> : since the new energies never assume the same value, this situation is called *anti-crossing.*

<p  align="center">
 <img src="./Images/image_3.png" width="60%" height="60%">
</p>

### Rabi oscillations

The Jaynes-Cummings Hamiltonian may be separated into two commuting parts:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?\hat{H}_{JC}&space;=&space;\hat{H}_0&space;&plus;&space;\hat{H}_{int}" title="\hat{H}_{JC} = \hat{H}_0 + \hat{H}_{int}" />
</p>

where <img src="https://latex.codecogs.com/svg.image?\hat{H}_0"> represents the Hamiltonian for the field plus the atom and <img src="https://latex.codecogs.com/svg.image?\hat{H}_{int}"> represents the field-atom interaction. All the dynamics of the system are contained in the second part.

Since it is assumed that the only states involved in the emission and absorption processes are <img src="https://latex.codecogs.com/svg.image?|g,n\rangle"> and <img src="https://latex.codecogs.com/svg.image?|e,n-1\rangle">, the state function <img src="https://latex.codecogs.com/svg.image?|\Psi(t)\rangle"> will be a linear combination of the two states with time-dependent coefficients; this means the system will oscillate over time between one state and another:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?|\Psi(t)\rangle&space;=&space;C_i(t)|i\rangle+C_f(t)f\rangle"/>
</p>

We can now assume that the initial state is <img src="https://latex.codecogs.com/svg.image?|i\rangle&space;=&space;|g,n\rangle"> and that the final state is <img src="https://latex.codecogs.com/svg.image?|f\rangle&space;=&space;|e,n-1\rangle"> this choice translates into the initial conditions:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?C_i(0)&space;=&space;1\qquad&space;C_f(0)&space;=&space;0"/>
</p>

The Schrodinger equation in the interaction picture is given by:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?i\hbar&space;\frac{|\Psi(t)\rangle}{dt}&space;=&space;\hat{H}_{int}&space;|\Psi(t)\rangle"/>
</p>

and this allows to write down differential equations for the coefficients <img src="https://latex.codecogs.com/svg.image?C_i(t)"> and <img src="https://latex.codecogs.com/svg.image?C_f(t)"> :

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?\dot{C}_i&space;&space;=&space;-i&space;\frac{1}{2}\Omega&space;\sqrt{n}\,C_f"/><br>
 <img src="https://latex.codecogs.com/svg.image?\dot{C}_f&space;&space;=&space;-i&space;\left(&space;\frac{1}{2}\Omega&space;\sqrt{n}\,C_i&space;&plus;&space;\Delta&space;C_f&space;\right)"/>
</p>

Substituting the first equation into the second and imposing the initial conditions we obtain:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?C_i&space;(t)&space;&space;=&space;i&space;\frac{\Omega}{\Omega_n}\cos\left(\frac{\Omega_n&space;t}{2}\right)&space;e^{i\Delta&space;t&space;/2}"/><br>
 <img src="https://latex.codecogs.com/svg.image?C_f&space;(t)&space;&space;=&space;-i&space;\frac{\Omega}{\Omega_n}\sin\left(\frac{\Omega_n&space;t}{2}\right)&space;e^{i\Delta&space;t&space;/2}"/>
</p>

With these coefficients, is possible to determine the probability of the system remains in the ground state <img src="https://latex.codecogs.com/svg.image?P_i(t)&space;=&space;|C_i(t)|^2">  and the probability it makes a transition to the excited state <img src="https://latex.codecogs.com/svg.image?P_f(t)&space;=&space;|C_f(t)|^2">. The atomic inversion then is given by:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?W_n(t)&space;=&space;P_f(t)&space;-&space;P_i(t)&space;=-&space;\frac{\Delta^2}{\Omega_n^2}&space;-&space;\frac{\Omega^2n}{\Omega_n^2}&space;\cos(\Omega_n&space;t)"/>
</p>

The configuration associated with  <img src="https://latex.codecogs.com/svg.image?W(t)&space;=&space;1"> can be reached only when there is perfect resonance.
Is interesting to see that in the absence of light (<img src="https://latex.codecogs.com/svg.image?n&space;=&space;0">), there is still a non-zero transition probability: this phenomenon is known as *vacuum Rabi oscillations*.

<p  align="center">
 <img src="./Images/output_Dirac.png" width="90%" height="90%">
</p>

### Initial conditions: mixtures

With the introduction of a Hamiltonian one has, in principle, established the time evolution of a quantum system. To complete the definition of a model one must also specify initial conditions.  
Over the years there have been studies of the JCM interacting with a great variety of initial single-mode fields, each with different statistical properties. These studies have shown that there can be remarkable differences in the behavior of the system with different initial conditions.
Assuming the atom in the ground state, the *initial states* of the atom and the field are:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?|\Psi_a(0)\rangle&space;&space;=&space;|g\rangle"/><br>
 <img src="https://latex.codecogs.com/svg.image?|\Psi_f(0)\rangle&space;&space;=&space;\sum_{n=0}^\infty&space;C_n|n\rangle"/>
</p>

While the initial state of the complete system is given by:

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?|\Psi(0)\rangle&space;=&space;|\Psi_{a}(0)\rangle&space;\otimes&space;|\Psi_{f}(0)\rangle"/>
</p>

In this case, to get the inversion function, all the functions <img src="https://latex.codecogs.com/svg.image?W_n(t)"> should be multiplied by the coefficients <img src="https://latex.codecogs.com/svg.image?|C_n|^2"> and added up.

<p align="center">
 <img src="https://latex.codecogs.com/svg.image?W(t)&space;=&space;-|C_0|^2&space;-&space;\sum_{n=0}^\infty&space;|C_n|^2&space;\left(&space;\frac{\Delta^2}{\Omega_n^2}&space;&plus;&space;\frac{\Omega^2n}{\Omega_n^2}&space;\cos(\Omega_n&space;t)\right)"/>
</p>

- An important example occurs when two-state atoms encounter a cavity maintained at a finite temperature <img src="https://latex.codecogs.com/svg.image?T">, so that the photon number distribution is that of one mode of [*black-body radiation*](https://en.wikipedia.org/wiki/Black-body_radiation), given by the [**Bose-Einstein probability distribution**](https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_statistics):

<p align="center"><img src="https://latex.codecogs.com/svg.image?|C_n|^2&space;=&space;P_n(T)&space;=&space;&space;&space;&space;\frac{1}{1&plus;\bar{n}}&space;&space;&space;&space;&space;\left(\frac{\bar{n}}{1&plus;\bar{n}}\right)^n"></p>

This distribution (termed *thermal* or *chaotic*) maximizes the field entropy for fixed mean photon number <img src="https://latex.codecogs.com/svg.image?|C_n|^2"> <img src="https://latex.codecogs.com/svg.image?\bar{n}">:

<p align="center"> <img src="https://latex.codecogs.com/svg.image?\bar{n}&space;=&space;\left(&space;&space;&space;&space;e^{\frac{\hbar&space;\omega_0}{k_B&space;T}}&space;-1&space;\right)^{-1}" /></p>

It is found that populations, for an average number of photons greater than 0, they no longer oscillate in a sinusoidal way: there is almost no trace of population oscillations and after an initial collapse we can observe irregular fluctuations. Furthermore, collapse is found to occur at a precise time scale <img src="https://latex.codecogs.com/svg.image?t_c">, fixed by the generalized Rabi frequency. For very large <img src="https://latex.codecogs.com/svg.image?\bar{n}"> we find that: <img src="https://latex.codecogs.com/svg.image?t_c=2/\Omega_n">.

<p  align="center">
 <img src="./Images/output_BoseEinstein.png" width="90%" height="90%">
</p>

- In the atom-field interaction, one of the most interesting phenomena is the *collapse-revival effect* in population inversion of atomic levels. To see this behavior we have to consider the initial condition in which the field is in a [*coherent state*](https://en.wikipedia.org/wiki/Coherent_state). In this case the number of photons follows a [**Poisson distribution**](https://en.wikipedia.org/wiki/Poisson_distribution):

 <p align="center"><img src="https://latex.codecogs.com/svg.image?|C_n|^2&space;=&space;P_n(\alpha)&space;=&space;&space;&space;&space;&space;\frac{\bar{n}^n}{n!}&space;e^{-\bar{n}}"></p>
 
 where <img src="https://latex.codecogs.com/svg.image?\bar{n}&space;=&space;|\alpha|^2">. It is natural to investigate this type of initial condition since coherent states are often described as states which have the dynamics most closely resembling the oscillatory behavior of a classical harmonic oscillator.\
 As with a thermal cavity, it was found that the Rabi oscillations do not persist indefinitely when the field is initially prepared in a coherent state. Instead, the oscillations collapse to yield constant populations.\
 As the field becomes more intense, and the mean photon number larger, the Rabi oscillations persist for longer intervals, but inevitably the incommensurability of Rabi oscillations for different photon numbers acts to wash out the periodicity of population transfers.\
 What was much more remarkable than the collapses, and unforeseen, was that the Rabi oscillations should revive after a quiescent interval. This *revival time* is essentially the inverse of the separation between distinct Rabi frequencies: <img src="https://latex.codecogs.com/svg.image?t_r&space;=&space;2\pi\sqrt{\bar{n}}\,t_c">.

<p  align="center">
 <img src="./Images/output_Poisson.png" width="90%" height="90%">
</p>


## Repository Structure

The repository is structured in the following folders:

### [Classes](https://github.com/soniasalomoni/Rabi_oscillations_JCM/tree/main/Classes)

This folder contains the definitions of the classes required to run the simulation. Each class is a container that collects and organizes the input data according to a physical meaning and logic. This is the hierarchical structure of the classes:

<p  align="center">
 <img src="./Images/schema.PNG" width="90%" height="90%">
</p>

- **`Field.py`:** this class stores the parameters that describe the cavity field  (`avg_n` the *average number of photons* <img src="https://latex.codecogs.com/svg.image?\bar{n}">, `pdf_n` the *probability density function of photons*, `cut_n` the *cut-off number of photons*). In addition, the class implements three physically relevant probability distributions of photons: `Dirac`, `Poisson`, and `BoseEinstein`.
- **`Atom.py`:** this class stores the parameters that describe the state of the atom in the cavity (`Cg` the *initial ground state coefficient*, `Ce` the *initial excited state coefficient)*.
- **`System.py`:** this class stores a `Field` and an `Atom` instances. In addition, the class is enriched by some interaction parameters (`int_coupling` the *interaction coupling* <img src="https://latex.codecogs.com/svg.image?\Omega">, `int_detuning` the *interaction detuning* <img src="https://latex.codecogs.com/svg.image?\Delta">).
The class implements a set of complex differential equations through the method `Rabi_model` that models the time evolution of the system using the Jaynes-Cummings model Hamiltonian.
- **`Simulation.py`:** this class contains a `System` instance and time information required to run a simulation on it (`time` the *simulation duration*, `tstep` the *simulation time step*). In particular, it is defined an odeint-like function for complex-valued differential equations `odeintz`.

### [Utilities](https://github.com/soniasalomoni/Rabi_oscillations_JCM/tree/main/Utilities)

This folder contains several files that are required to run the simulation. In particular, we distinguish:

- **`input.txt`:** this is the configuration file, where we set all the simulation parameters.
- **`reqs.txt`:** this file contains the dependencies needed in order to run the simulation.
- **`saving.py`:** this file produces a **.txt** file containing the inversion function if `save_txt` is set to `True`.
- **`plotting.py`:** this file handles the graphical visualization of the inversion function. The plot is saved as a **.png** file if `save_png` is set to `True`.

### [Testing](https://github.com/soniasalomoni/Rabi_oscillations_JCM/tree/main/Testing)

In this folder, the main functions of the program are tested. The testing is performed using the library [hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html). Two types of testing are performed:

- **`prop_test.py`:** in this file we make sure that the **Field methods** `Dirac`, `Poisson`, and `BoseEinstein` are actually PDFs, thus we test that:

    - PDF(<img src="https://latex.codecogs.com/svg.image?n">) is non-negative for all possible values of n.
    - PDF(<img src="https://latex.codecogs.com/svg.image?n">) over all possible values of <img src="https://latex.codecogs.com/svg.image?n"> is normalized.

- **`oracle_test.py`:** in this file we check that the numerical solution that we obtain executing the simulation is compatible with the analytical solution provided by the theory. With this test we make sure that the algorithm used to solve the complex-differential equation is correct.
An analytical solution is only available in this simplified case; if we want to extend our model to effects not considered so far, the numerical solution becomes the only viable one.

### [Output](https://github.com/soniasalomoni/Rabi_oscillations_JCM/tree/main/Output)

This folder will contain the **.txt** and **.png** files if `save_txt` and  `save_png` in the `input.txt` file are set to `True`. The name of the file is specified by `out_label`. The **.png** file can be used to verify the expected behavior, while the **.txt** files can be used to build more complex graphical representation.

### [Jobs](https://github.com/soniasalomoni/Rabi_oscillations_JCM/tree/main/Jobs)

This folder contains two *jobscripts* (**.sh** files) containing the setup information needed to automatize the run of `Rabi.py` on different input files:

- **`jobPDF.sh`:** this jobscript runs Rabi.py changing the type of PDF `pdf_n` (*Dirac*, *Poisson*, *BoseEinstein*) and keeping unchanged the rest of input parameters. The label of the output files are also modified accordingly in order to not override them.
- **`jobAVGn.sh`:** this jobscript runs Rabi.py changing the average number of photons  `avg_n` (**10**, **30**, **50**) for a field in a coherent state and keeping unchanged the rest of input parameters. The label of the output files are also modified accordingly in order to not override the files. One can modify the selected PDF to observe the different behavior of Rabi oscillations in function of <img src="https://latex.codecogs.com/svg.image?\bar{n}">.

## Usage

To clone the repository type:
```bash
git clone https://github.com/soniasalomoni/Rabi_oscillations_JCM.git
cd Rabi_oscillations_JCM
```
To install the dependencies type the command:
```bash
pip install -r Utilities/reqs.txt
```

To launch the main script `Rabi.py`, with the possibility to specify the configuration file as `sys.argv[1]`, type the command:
```bash
python Rabi.py my_input_file.txt
```

The default configuration file if not specified through `sys.argv[1]` is `input.txt`.

To run a test, for example `prop_test.py`, type the command:
```bash
pytest prop_test.py
```

To run a jobscript, for example `jobPDF.sh`, first type this command to make the script executable:
```bash
chmod u+x jobPDF.sh
```
Then:
```
./Jobs/jobPDF.sh
```
