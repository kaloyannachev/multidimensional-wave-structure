import numpy as np
import matplotlib.pyplot as plt
from .dimensional_relations import c_D, E_massive_ratio, E_photon_ratio, R_ratio
from .plotting import setup, savefig

def fig_energy_scaling():
    setup(); D = np.linspace(1.5, 10, 500)
    plt.plot(D, E_massive_ratio(D), label=r"massive: $D/3$")
    plt.plot(D, E_photon_ratio(D), linestyle="--", label=r"photon: $\\sqrt{D/3}$")
    plt.xlabel("Dimension $D$"); plt.ylabel("Normalized energy"); plt.legend()
    savefig("figures/fig_energy_scaling_unified.pdf")

def fig_curvature_scaling():
    setup(); D = np.linspace(1.5, 10, 500)
    plt.semilogy(D, R_ratio(D))
    plt.xlabel("Dimension $D$"); plt.ylabel(r"$R_D/R_{3D}$ (log)")
    savefig("figures/fig_curvature_scaling_unified.pdf")

def fig_combined():
    setup(); D = np.linspace(1.5, 10, 500)
    delta_gamma = D/3.0 - 1.0
    alpha = 0.5*(1 + 3.0/D)
    ax1 = plt.gca()
    ax1.plot(D, delta_gamma, label=r"$\\Delta\\gamma$")
    ax1.set_xlabel("Dimension $D$"); ax1.set_ylabel(r"$\\Delta\\gamma$")
    ax2 = ax1.twinx()
    ax2.plot(D, alpha, linestyle="--", label=r"$\\alpha$")
    ax2.set_ylabel(r"$\\alpha$")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.15))
    savefig("figures/combined_dimensional_dependencies_unified.pdf")

def main():
    fig_energy_scaling()
    fig_curvature_scaling()
    fig_combined()

if __name__ == "__main__":
    main()
