import numpy as np
import matplotlib.pyplot as plt

def scatter_plot():
    # Generar datos
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.tanh(x)

    # Crear la figura y los ejes
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)  # 1 fila, 1 columna, primer gráfico

    # Graficar la función tanh(x) con scatter
    ax.scatter(x, y, c='darkcyan', marker='o', label='y = tanh(x)')

    # Configurar el gráfico
    ax.set_facecolor('whitesmoke')
    ax.grid('solid')
    ax.set_title('Scatter Plot de tanh(x)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()

    # Mostrar el gráfico
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Scatter Plot")

    scatter_plot()

    print("terminamos")