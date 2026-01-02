import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # required for 3D
from sklearn.linear_model import LinearRegression

# ----- 1) Generate synthetic data -----
np.random.seed(1)
n = 120
x2 = np.random.normal(50, 10, n)           # predictor 2
x1 = 0.5 * x2 + np.random.normal(0, 5, n)  # predictor 1 (correlated with x2)
y  = 300 + 2*x1 - 1.5*x2 + np.random.normal(0, 5, n)  # outcome

# Stack predictors into a 2D array for sklearn and fit MLR: y ~ x1 + x2
X = np.column_stack([x1, x2])
model = LinearRegression().fit(X, y)
b0, b1, b2 = model.intercept_, *model.coef_
print(f"Fitted model: y = {b0:.2f} + {b1:.2f}*x1 + {b2:.2f}*x2")

# ----- 2) Regression plane -----
x1_lin = np.linspace(x1.min(), x1.max(), 40)
x2_lin = np.linspace(x2.min(), x2.max(), 40)
X1g, X2g = np.meshgrid(x1_lin, x2_lin)
Yg = b0 + b1 * X1g + b2 * X2g

# ----- 3) Lines on the plane for fixed x2 values -----
# Choose the x2 levels you want to "hold constant" here:
x2_levels = [np.percentile(x2, p) for p in (20, 50, 80)]  # or e.g., [40, 50, 60]
x1_line = np.linspace(x1.min(), x1.max(), 100)

# Base z level for projecting lines onto the x1–x2 plane (for visualization)
z_base = y.min() - 10

# ----- 4) Plot -----
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter observed data
ax.scatter(x1, x2, y, alpha=0.35, s=14)

# Regression plane
ax.plot_surface(X1g, X2g, Yg, alpha=0.35, rstride=1, cstride=1, linewidth=0, antialiased=True)

# Lines for fixed x2 values + their projections on the x1–x2 plane
for lvl in x2_levels:
    y_line = b0 + b1 * x1_line + b2 * lvl
    ax.plot(x1_line, np.full_like(x1_line, lvl), y_line, label=f"x2 = {lvl:.1f}")
    ax.plot(x1_line, np.full_like(x1_line, lvl), np.full_like(x1_line, z_base), linestyle='--')

# Draw a faint "ground" plane at z = z_base
X1g2, X2g2 = np.meshgrid(np.linspace(x1.min(), x1.max(), 2),
                         np.linspace(x2.min(), x2.max(), 2))
Zg2 = np.full_like(X1g2, z_base)
ax.plot_surface(X1g2, X2g2, Zg2, alpha=0.08)

# Labels and legend
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")
ax.set_title("Lines on the regression plane for fixed x2 (with projections)")
ax.legend()

plt.show()
