import numpy as np
import matplotlib.pyplot as plt
from solver import theta,M,X,tu,xe,ye,result
r=np.radians(theta)
A=np.exp(M*np.abs(tu))*np.sin(0.3*tu)
xp=tu*np.cos(r)-A*np.sin(r)+X
yp=42+tu*np.sin(r)+A*np.cos(r)

plt.figure(figsize=(10,6))
plt.scatter(
    xe[::15],
    ye[::15],
    s=45,
    facecolors="none",edgecolors="deepskyblue",linewidths=1.8,label="expected curve samples",zorder=3
)
plt.plot(
    xp,yp,color="red",linewidth=2,label="predicted curve",zorder=2
)
plt.xlabel("X")
plt.ylabel("Y")
plt.title(
    "expected vs predicted curve\n"
    f"θ={theta:.5f}°, M={M:.8f}, X={X:.5f} | "

    f"Mean L1={result.fun / len(tu):.8f}"
)
plt.legend()

plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    "plots/final_curve_comparison.png",
)
plt.show()