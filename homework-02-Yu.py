#%%-2
import numpy as np
def problem_02(a, b, c):
    X = a + (b - a) * np.random.rand(100)
    mask = X < c
    return np.sum(mask)

#%%-3
import numpy as np
def problem_03():
    X = np.random.rand(5, 5)
    return X[[0, 2], 1:5]

#%%-4
def problem_04(N):
    X = np.zeros((N, N), dtype=int)
    X[0, :] = 1
    X[-1, :] = 1
    X[:, 0] = 1
    X[:, -1] = 1
    return X

#%%-5
def least_squares_error(x, y):
    return np.sum((x - y) ** 2)

#%%-6
def normalized_random(N):
    X = np.random.rand(N, N)
    row_sums = np.sum(X, axis=1)
    return X / row_sums[:, np.newaxis]

#%%-7
import numpy as np
import matplotlib.pyplot as plt

def problem_07():
    # Graph 1: x^2
    X = np.linspace(0, 10, 1000)
    Y = X ** 2
    plt.figure()
    plt.plot(X, Y, label="f(x) = x^2")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Graph 1: f(x) = x^2")
    plt.legend()
    plt.savefig("graph1_x_squared.png")
    plt.close()

    # Graph 2: sin(x) and cos(x)
    X = np.linspace(-np.pi, np.pi, 1000)
    Y1 = np.sin(X)
    Y2 = np.cos(X)
    plt.figure()
    plt.plot(X, Y1, label="f(x) = sin(x)")
    plt.plot(X, Y2, label="g(x) = cos(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph 2: sin(x) and cos(x)")
    plt.legend()
    plt.savefig("graph2_sin_cos.png")
    plt.close()

    # Graph 3: arctan(x) and logistic function
    X = np.linspace(0, 5, 1000)
    Y1 = np.arctan(X)
    Y2 = 1 / (1 + np.exp(-X))
    plt.figure()
    plt.plot(X, Y1, label="f(x) = arctan(x)")
    plt.plot(X, Y2, label="g(x) = 1 / (1 + e^(-x))")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph 3: arctan(x) and logistic function")
    plt.legend()
    plt.savefig("graph3_arctan_logistic.png")
    plt.close()

#%%-8
import numpy as np
import time

def sort_times():
    N = 10_000_000
    repeats = 10
    integer_results = []
    float_results = []

    # Random integers
    for i in range(repeats):
        L = list(np.random.randint(0, 1000000, N))
        a = np.array(L)
        start = time.time()
        np.sort(a)
        end = time.time()
        array_time = end - start
        start = time.time()
        L.sort()
        end = time.time()
        list_time = end - start
        integer_results.append((i + 1, array_time, list_time))

    # Random floats from 0 to 1
    for i in range(repeats):
        L = list(np.random.rand(N))
        a = np.array(L)
        start = time.time()
        np.sort(a)
        end = time.time()
        array_time = end - start
        start = time.time()
        L.sort()
        end = time.time()
        list_time = end - start
        float_results.append((i + 1, array_time, list_time))

    print("Integer results:")
    for row in integer_results:
        print(row)

    print("Float results:")
    for row in float_results:
        print(row)
sort_times()
