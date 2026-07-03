import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]
data_path = project_dir / "data" / "xy_data.csv"
plots_dir = project_dir / "plots"

plots_dir.mkdir(exist_ok=True)

df = pd.read_csv(data_path)

#overview
print("="*60)
print("dataset shape")
print(df.shape)
print("\ncolumn names")
print(df.columns)
print("\nfirst 5 rows")
print(df.head())
print("\nlast 5 rows")
print(df.tail())
print("\nstatistical summary")
print(df.describe())
print("\nMissing values")
print(df.isnull().sum())

#scatter plot of x and y
plt.figure(figsize=(8,6))
plt.scatter(df["x"],df["y"],s=3)
plt.title("Figure1:distribution of sampled points")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.tight_layout()
plt.savefig(plots_dir/"figure_1_sampled_points.png",dpi=300)
plt.close()

#point plot of x and y across the dataset
plt.figure(figsize=(10, 5))
plt.plot(df.index,df["x"],label="X")
plt.plot(df.index,df["y"],label="Y")
plt.title("Figure2:X and Y Values Across Given Dataset")
plt.xlabel("Sample Index")
plt.ylabel("Coordinate Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(plots_dir/"figure_2_xy_across_dataset.png",dpi=300)
plt.close()

#histogram of x 
plt.figure(figsize=(8,5))
plt.hist(df["x"],bins=40)
plt.title("Figure3:distribution of X")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.savefig(plots_dir/"figure_3_distribution_of_x.png",dpi=300)
plt.close()

#histogram of y
plt.figure(figsize=(8,5))
plt.hist(df["y"],bins=40)
plt.title("Figure4:distribution of Y")
plt.xlabel("Y")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.savefig(plots_dir/"figure_4_distribution_of_y.png",dpi=300)
plt.close()

#relationship between x and y
plt.figure(figsize=(8,6))
plt.scatter(df["x"],df["y"],s=2)
plt.title("Figure5:relationship between X and Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.tight_layout()
plt.savefig(plots_dir/"figure_5_relationship_between_x_y.png",dpi=300)
plt.close()
