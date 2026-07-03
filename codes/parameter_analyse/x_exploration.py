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
# X Exploration
# ---------------------------------
x_shift_values = [0, 20, 40, 60, 80]

plt.figure(figsize=(10, 7))

for X in x_shift_values:
    x, y = curve_gen(theta_deg=20, M=0, X=X)
    plt.plot(x, y, label=f"X = {X}")

plt.title("Effect of X on Horizontal Translation")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(plots_dir / "effect_of_X.png", dpi=300)
plt.show()