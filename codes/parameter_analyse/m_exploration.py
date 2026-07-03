import sys
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------
# Path Setup
# ---------------------------------
project_dir = Path(__file__).resolve().parents[2]
codes_dir = project_dir / "codes"
plots_dir = project_dir / "plots"

sys.path.append(str(codes_dir))
plots_dir.mkdir(exist_ok=True)

from curve_generator import curve_gen

# ---------------------------------
# M Exploration
# ---------------------------------
m_values = [-0.04, -0.02, 0, 0.02, 0.04]

plt.figure(figsize=(10, 7))

for m in m_values:
    x, y = curve_gen(theta_deg=20, M=m, X=0)
    plt.plot(x, y, label=f"M = {m}")

plt.title("Effect of M on Oscillation Amplitude")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(plots_dir / "effect_of_M.png", dpi=300)
plt.show()