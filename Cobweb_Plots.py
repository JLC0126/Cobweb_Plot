import matplotlib.pyplot as plt
from numpy import sin, cos, linspace

def cobweb(F, x0, N, a=0, b=1):
    # Mapa de F
    t = linspace(a, b, N)
    plt.plot(t, F(t), 'k')

    # Grafica de la recta y = x
    plt.plot(t, t, "r:")

    # Grafica las iteraciones 
    x, y = x0, F(x0)
    for _ in range(N):
        fy = F(y)
        plt.plot([x, y], [y,  y], 'b', linewidth=1)
        plt.plot([y, y], [y, fy], 'b', linewidth=1)
        x, y = y, fy

    plt.show()