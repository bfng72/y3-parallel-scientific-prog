import math
import random

def trapezium(u0, h, T, k):
    u = u0
    t = 0.0
    T = float(T)
    steps = round(T / h)

    for step in range(steps):
        # Direct implicit update for u_{n+1}
        numerator = (1 - (h * k) / 2) * u + ((h * k) / 2) * (
            math.cos(t) + math.cos(t + h)
        )
        denominator = 1 + (h * k) / 2

        u = numerator / denominator
        t += h

    exact = (k / (1 + k**2)) * (math.sin(T) + k * math.cos(T)) + (u0 - (k**2 / (1 + k**2))) * math.exp(-k * T)

    return u, exact


def euler(u0, h, T, k):
    u = u0
    t = 0.0
    T = float(T)
    steps = round(T / h)

    for step in range(steps):
        # Explicit Euler step
        u = u + h * (-k * (u - math.cos(t)))
        t += h

    exact = (k / (1 + k**2)) * (math.sin(T) + k * math.cos(T)) + (
        u0 - (k**2 / (1 + k**2))
    ) * math.exp(-k * T)

    return u, exact

print(f"Euler: {euler(1, 0.01, 1, 2)}")
print(f"Trapezium: {trapezium(1, 0.01, 1, 2)}")


def monte_carlo(N, x_1, x_2, height, func):
    def f1(x):
        return math.cos(x)*math.exp(-x)

    def f2(x):
        return (x**3) * math.exp(-x)

    hits = 0
    
    if func == "f1":
        for i in range(N):
            x = random.uniform(x_1, x_2)
            y = random.uniform(0, height)
            if y < f1(x):
                hits += 1
        return (hits / N) * (x_2 - x_1) * height
    elif func == "f2":
        for i in range(N):
            x = random.uniform(x_1, x_2)
            y = random.uniform(0, height)
            if y < f2(x):
                hits += 1
        return (hits / N) * (x_2 - x_1) * height

print(f"Monte Carlo: {monte_carlo(10000, 0, math.pi/2, 1, 'f1')}")
print(f"Monte Carlo: {monte_carlo(10000, 1, 6, 1, 'f2')}")
    
print(f"Monte Carlo: {monte_carlo(100000, 0, math.pi/2, 1, 'f1')}")
print(f"Monte Carlo: {monte_carlo(100000, 1, 6, 1, 'f2')}")