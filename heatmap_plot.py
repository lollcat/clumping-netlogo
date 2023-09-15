import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    fecundity = np.array([15., 5., 1.])
    dispersibility = np.array([1., 5., 15.])
    mean_over_var = np.array([[1., 1.4, 1.4], [0.2, 0.9, 1.0], [0.1, 0.7, 0.9]])
    var_over_mean = 1. / mean_over_var
    sns.heatmap(var_over_mean, xticklabels=dispersibility, yticklabels=fecundity, cmap='gray')
    plt.xlabel("Dispersibility")
    plt.ylabel("Fecundity")
    plt.tight_layout()
    plt.savefig("plant.png")
    plt.show()
