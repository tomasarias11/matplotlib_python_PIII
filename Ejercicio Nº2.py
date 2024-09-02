# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def multi_plot():
    # Dibujar múltiples líneas en un mismo gráfico
    x = list(np.linspace(-4, 4, 20))
    # Cálculo de las funciones
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    
    # Crear la figura y los ejes
    fig = plt.figure()
    ax = fig.add_subplot()

    # Graficar las dos funciones con diferentes colores y marcadores
    ax.plot(x, y1, color='blue', marker='^', label='y1 = x^2')
    ax.plot(x, y2, color='green', marker='*', label='y2 = x^3')
    # Configurar el gráfico
    ax.set_facecolor('ivory')
    ax.set_title("Dos funciones un mismo grafico")
    ax.set_ylabel("Y[amplitud]")
    ax.set_xlabel("X[rads]")
    ax.set_xlim([-4, 4])  # Limito el eje "X" entre -4 y 4
    ax.set_ylim([-70, 70])  # Limito el eje "Y" entre -70 y 70 (ajustado para ver la curva cúbica mejor)
    ax.legend()
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")

    # Crear el gráfico
    multi_plot()  

    print("terminamos")