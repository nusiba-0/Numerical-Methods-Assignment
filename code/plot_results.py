import matplotlib.pyplot as plt

def plot_interpolations(x, y, x_fine, y_spline, y_lagrange):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Data Points', markersize=8)
    plt.plot(x_fine, y_spline, label='Cubic Spline Interpolation', linewidth=2)
    plt.plot(x_fine, y_lagrange, label='Lagrange Interpolation', linestyle='--', linewidth=2)
    plt.title('Cubic Spline vs Lagrange Interpolation')
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../plots/interpolation_comparison_plot.png')
    plt.show()

