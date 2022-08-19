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

<img src="https://img.icons8.com/ios/50/000000/notion.png" width="30px" height="30px"> Check this [Notion page](https://sonia-salomoni.notion.site/The-Jaynes-Cummings-model-56651cd955934b1dae5f9bb668545a4f)  

**INDEX**
  
> [**Repository Structure**](#Repository-Structure)
> - [Classes](#Classes)
> - [Utilities](#Utilities)
> - [Testing](#Testing)
> - [Output](#Output)
> - [Jobs](#Jobs)
>
> [**Usage**](#Usage)


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

To **clone the repository** type:
```bash
git clone https://github.com/soniasalomoni/Rabi_oscillations_JCM.git
cd Rabi_oscillations_JCM
```
To **install the dependencies** type the command:
```bash
pip install -r Utilities/reqs.txt
```

To **launch the main script** `Rabi.py`, just type:
```bash
python Rabi.py
```
you also have the possibility to specify the name of the configuration file as `sys.argv[1]` (**input.txt** is the default configuration file), for example:
```bash
python Rabi.py my_input_file.txt
```

To **run a test**, for example `prop_test.py`, type the command:
```bash
pytest Testing/prop_test.py
```

To **run a jobscript**, for example `jobPDF.sh`, first type this command to make the script executable:
```bash
chmod u+x Jobs/jobPDF.sh
```
then:
```
./Jobs/jobPDF.sh
```
