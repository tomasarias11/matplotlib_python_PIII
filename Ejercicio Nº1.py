# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def line_plot():
    # Generaremos la función y=X^2 (x al cuadrado)
    x = list(range(-10, 11, 1))
    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)
    
    fig = plt.figure()
    fig.suptitle('Grafico: Y=X^2', fontsize=12)
    ax = fig.add_subplot()
    
    #Colocar la leyenda y el label con el nombre de la función y darle color a la línea a su elección
    ax.plot(x, y, c='blue', marker='^', label='función:y=x^2')
    ax.legend()
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.grid()
    ax.set_facecolor('lightyellow')
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")

    line_plot()

    print("terminamos")