import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-2*np.pi, 2*np.pi, 100)
funcion =np.cos(x)

plt.plot(x,funcion)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Grafica coseno")
plt.savefig("graficasen.png")


