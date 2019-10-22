import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-2*np.pi, 2*np.pi, 100)
funcion =np.sin(x)

plt.plot(x,funcion)
plt.show()
