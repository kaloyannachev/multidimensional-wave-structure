import matplotlib.pyplot as plt

def setup():
    plt.rcParams.update({
        "figure.figsize": (6,4),
        "font.size": 12,
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "lines.linewidth": 2,
    })

def savefig(path):
    plt.tight_layout()
    plt.savefig(path.replace(".pdf",".png"), dpi=200, bbox_inches="tight")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
