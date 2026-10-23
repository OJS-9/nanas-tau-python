"""Shared setup for every lecture: `from py.setup import *` (or `import sys; sys.path.insert(0, "..")`
then `from py.setup import nanas_pal, apply_nanas_theme`) in the first chunk.
Keeps the look of all charts consistent across the course. Python port of R/setup.R.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd

RNG_SEED = 2026
rng = np.random.default_rng(RNG_SEED)

# Colour-blind safe palette (Okabe-Ito based). Same hex values as R/setup.R's nanas_pal.
nanas_pal = {
    "primary": "#2B59C3",
    "accent": "#E4572E",
    "green": "#009E73",
    "yellow": "#E69F00",
    "sky": "#56B4E9",
    "purple": "#8E6BBF",
    "grey": "#8A8F98",
}
nanas_palette = list(nanas_pal.values())


def apply_nanas_theme(base_size: int = 14) -> None:
    """Apply the course-wide matplotlib/seaborn theme (Python port of theme_nanas())."""
    sns.set_theme(style="whitegrid", palette=nanas_palette)
    mpl.rcParams.update(
        {
            "font.size": base_size,
            "axes.titlesize": base_size + 2,
            "axes.titleweight": "bold",
            "axes.titlelocation": "right",   # Hebrew titles align right
            "axes.grid": True,
            "grid.linewidth": 0.5,
            "axes.edgecolor": "#8A8F98",
            "figure.dpi": 150,
            "savefig.dpi": 150,
            "legend.frameon": False,
            "legend.loc": "upper right",
        }
    )


apply_nanas_theme()
pd.set_option("display.precision", 4)
pd.set_option("display.width", 120)

__all__ = ["nanas_pal", "nanas_palette", "apply_nanas_theme", "rng", "RNG_SEED"]
