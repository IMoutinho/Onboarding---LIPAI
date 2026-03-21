import matplotlib.pyplot as plt
import numpy as np


# matplotlib

t = np.linspace(0, 2*np.pi, 10000)

y = np.cos(4*t)

print(y)

plt.plot(t, y)
plt.title('Gráfico do Cosseno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()

