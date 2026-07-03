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
# Theta Exploration
# ---------------------------------
theta_values = [0, 10, 20, 30, 40, 50]

plt.figure(figsize=(10, 7))

for theta in theta_values:
    x, y = curve_gen(theta_deg=theta, M=0, X=0)
    plt.plot(x, y, label=f"theta = {theta}°")

plt.title("Effect of Theta on Curve Orientation")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(plots_dir / "effect_of_theta.png", dpi=300)
plt.show()