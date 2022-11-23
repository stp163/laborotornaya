def F(a, b, c):
    D = ((b ** 2) - 4 * a * c) ** 0.5
    x1 = (-b + D) / 2 * a
    x2 = (-b - D) / 2 * a
    return x1, x2
