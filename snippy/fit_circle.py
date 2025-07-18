import numpy as np

def generate_points(n, sigma):
    """Generate a series of random points uniformly on a circle.
    """
    # Extract the data points.
    phi = np.linspace(0.0, 2.0 * np.pi, n)
    x = np.sin(phi)
    y = np.cos(phi)
    # Add the measurement errors.
    x = x + np.random.normal(0.0, sigma, n)
    y = y + np.random.normal(0.0, sigma, n)
    return x, y

def fit_circle(x, y, sigma):
    """Fit a series of data points to a circle.
    """
    n = len(x)
    # Refer coordinates to the mean values of x and y.
    x_m = np.mean(x)
    y_m = np.mean(y)
    u = x - x_m
    v = y - y_m
    # Calculate all the necessary sums.
    s_u = np.sum(u)
    s_uu = np.sum(u**2.0)
    s_uuu = np.sum(u**3.0)
    s_v = np.sum(v)
    s_vv = np.sum(v**2.0)
    s_vvv = np.sum(v**3.0)
    s_uv = np.sum(u * v)
    s_uuv = np.sum(u * u * v)
    s_uvv = np.sum(u * v * v)
    D = 2.0 * (s_uu * s_vv - s_uv**2.0)
    # Calculate the best-fit values.
    u_c = (s_vv * (s_uuu + s_uvv) - s_uv * (s_vvv + s_uuv)) / D
    v_c = (s_uu * (s_vvv + s_uuv) - s_uv * (s_uuu + s_uvv)) / D
    x_c = u_c + x_m
    y_c = v_c + y_m
    r = np.sqrt(u_c**2.0 + v_c**2.0 + (s_uu + s_vv) / n)
    # Calculate the errors---mind this is only rigorously valid
    # if the data points are equi-spaced on the circumference.
    sigma_xy = sigma * np.sqrt(2.0 / n)
    sigma_r = sigma * np.sqrt(1.0 / n)
    return  x_c, y_c, r, sigma_xy, sigma_r

# Uncertainty on x and y, assumed to be the same for all the
# data points, in both coordinates.
np.random.seed(1)
sigma = 0.05
x, y = generate_points(25, sigma)
x_c, y_c, r, sigma_xy, sigma_r = fit_circle(x, y, sigma)

print(f'x_c = {x_c:.3f} +/- {sigma_xy:.3f}')
print(f'y_c = {y_c:.3f} +/- {sigma_xy:.3f}')
print(f'r = {r:.3f} +/- {sigma_r:.3f}')
