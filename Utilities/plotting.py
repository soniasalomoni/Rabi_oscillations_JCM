
import matplotlib.pyplot as plt

# define plotting function

def plot_W(simulation):
    """
    Plot simulation results (atomic inversion function)

    Parameters:
    -----------
    simulation : Simulation 
        the Simulation instance whose inversion function is plotted
    
    Return:
    -------
    fig : Figure

    """
    fig, ax = plt.subplots(figsize=(7,3))
    ax.plot(simulation.time,simulation.W_array,label='W(t)')
    ax.set(title='Inversion function',xlabel='time [s]')
    ax.set(ylim=[-1.15,1.15])
    ax.legend(loc = 'lower right')
    ax.grid(color='gray',alpha=0.8, linestyle='--')
    fig.tight_layout()
    return fig