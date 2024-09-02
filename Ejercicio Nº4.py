import numpy as np
import matplotlib.pyplot as plt

def grid():
    # Generar los valores de X
    x = np.linspace(0, 10, 40)
    
    # Calcular las funciones
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)
    
    # Crear la figura y los ejes
    fig = plt.figure()
    fig.suptitle('Grafico con 4 funciones', fontsize=16)

    # Gráfico 1: y1 = x**2
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x, y1, color='red', label='y1 = x^2')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(ls='dashed')
    ax1.set_ylabel("Y[amplitud]")
    ax1.set_xlabel("X[rads]")
    ax1.legend()

    # Gráfico 2: y2 = x**3
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(x, y2, color='green', label='y2 = x^3')
    ax2.set_facecolor('whitesmoke')
    ax2.grid(ls='dashed')
    ax2.set_ylabel("Y[amplitud]")
    ax2.set_xlabel("X[rads]")
    ax2.legend()

    # Gráfico 3: y3 = x**4
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(x, y3, color='blue', label='y3 = x^4')
    ax3.set_facecolor('whitesmoke')
    ax3.grid(ls='dashed')
    ax3.set_ylabel("Y[amplitud]")
    ax3.set_xlabel("X[rads]")
    ax3.legend()

    # Gráfico 4: y4 = sqrt(x)
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(x, y4, color='orange', label='y4 = sqrt(x)')
    ax4.set_facecolor('whitesmoke')
    ax4.grid(ls='dashed')
    ax4.set_ylabel("Y[amplitud]")
    ax4.set_xlabel("X[rads]")
    ax4.legend()
    
    # Mostrar la figura con los cuatro gráficos
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot: Figura con múltiples gráficos")

    grid()

    print("terminamos")