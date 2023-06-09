import numpy as np

def runge_kutta_system_integration(f, t0, y0, h, n):
    """
    Función para realizar la integración numérica utilizando el método de Runge-Kutta de orden 4 para sistemas de n ecuaciones diferenciales.

    Parámetros:
    - f: Una función que describe el sistema de ecuaciones diferenciales dy/dt = f(t, y), donde t es el tiempo y y es una lista con los valores de las variables.
    - t0: El valor inicial de t.
    - y0: Una lista con los valores iniciales de las variables.
    - h: El tamaño del paso.
    - n: El número de iteraciones.

    Retorna:
    - Una lista de listas con los valores de t y las variables y en cada paso.
    """
    t_values = [t0]
    y_values = [y0]

    for i in range(n):
        t = t_values[-1]
        y = y_values[-1]

        k1 = h * np.array(f(t, y))
        k2 = h * np.array(f(t + h/2, y + k1/2))
        k3 = h * np.array(f(t + h/2, y + k2/2))
        k4 = h * np.array(f(t + h, y + k3))

        y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t_new = t + h

        t_values.append(t_new)
        y_values.append(y_new)

    return t_values, y_values


def equations(t, y):
    """
    Una función que describe el sistema de ecuaciones diferenciales dy/dt = f(t, y),
    donde t es el tiempo y y es una lista con los valores de las variables.
    """
    # Implementa aquí las ecuaciones diferenciales del sistema
    # Puedes utilizar cualquier número de ecuaciones

    # Ejemplo de sistema de 3 ecuaciones diferenciales
    dydt = [
        y[1],
        -y[0] + y[2],
        np.sin(y[0]) - np.cos(y[1])
    ]
    
    return dydt


# Parámetros de integración
t0 = 0  # Valor inicial de t
y0 = [1, 0, np.pi/4]  # Valores iniciales de las variables
h = 0.1  # Tamaño del paso
n = 10  # Número de iteraciones

# Realizar la integración
t_values, y_values = runge_kutta_system_integration(equations, t0, y0, h, n)

# Imprimir los resultados
for t, y in zip(t_values, y_values):
    print(f"t = {t}, y = {y}")
