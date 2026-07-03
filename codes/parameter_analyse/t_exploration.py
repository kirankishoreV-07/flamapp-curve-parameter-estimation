import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------
# Path Setup
# ---------------------------------
project_dir = Path(__file__).resolve().parents[2]
plots_dir = project_dir / "plots"

plots_dir.mkdir(exist_ok=True)

# ---------------------------------
# t Exploration
# ---------------------------------
t = np.linspace(6, 60, 1000)
wave = np.sin(0.3 * t)

plt.figure(figsize=(10, 5))
plt.plot(t, wave)

plt.title("Behaviour of sin(0.3t)")
plt.xlabel("t")
plt.ylabel("sin(0.3t)")
plt.grid(True)
plt.tight_layout()

plt.savefig(plots_dir / "behaviour_of_sin_03t.png", dpi=300)
plt.show()