import math

def calculate_air_resistance(v, c, a, p):
    """Calculate air resistance given velocity, coefficient, area, and density."""
    return 0.5 * c * a * p * v**2

def calculate_terminal_velocity(m, g, c, a, p):
    """Calculate terminal velocity given mass, gravity, coefficient, area, and density."""
    return math.sqrt((2 * m * g) / (c * a * p))
