import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-2*np.pi, 2*np.pi, 100)
funcion =np.sin(x)

plt.plot(x,funcion)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Grafica seno")
plt.savefig("graficasen.png")
