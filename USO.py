import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import matrix_rank
from numpy.linalg import inv

#2.1
print("2.1")
#a)
a1 = 3**12
b1 = 5
x1 = a1 - b1
print("a)", x1)

#b)
a2 = np.array([2,0.5])
b2 = np.array([[1,4],[-1,3]])
c2 = np.array([[-1],[-3]])
x2 = a2 @ b2 @ c2
print("b)",x2)

#c)
a3 = np.array([[1,-2,0],[-2,4,0],[2,-1,7]])
x3 = matrix_rank(a3)
print("c)",x3)

#d)
a4 = np.array([[1,2],[-1,0]])
b4 = np.array([[-1],[2]])
x4 = inv(a4) @ b4
print("d)",x4,"\n")


#2.2
a5 = [1,1,-129,171,1620]
def funkcja1():
    x_1 = np.polyval(a5,-46)
    x_2 = np.polyval(a5,14)
    print("2.2")
    print("Współczynniki wynoszą: ", x_1," ",x_2,"\n")
    

#3.1
def funkcja2():
    x_start = -46
    x_end = 14
    
    #3.3
    acc = 1000  #dokładność

    interval = np.linspace(x_start, x_end ,acc)
    all_values = np.polyval(a5,interval)
    min_val = np.min(all_values)
    max_val = np.max(all_values)
    print("3.1")
    print("Maksymalna wartość w przedziale: ",max_val)
    print("Minimalna wartość w przedziale: ",min_val,"\n")

#4.1/4.2/5.1/5.2
def funkcja3(given_var, x_start, x_end, acc):
    var_size = np.size(given_var)
    interval = np.linspace(x_start, x_end ,acc) #przedział
    all_values = np.polyval(given_var,interval) #wartośc wielomianów
    min_val = np.min(all_values)
    max_val = np.max(all_values)
    min_val_index = np.argmin(all_values)
    max_val_index = np.argmax(all_values)

    #ekstrema
    min_point = (interval[min_val_index], min_val)
    max_point = (interval[max_val_index], max_val)

    print("4.1/4.2/5.1/5.2")
    print("Stopień wielomianu: ",var_size)
    print("Wybrane współczynniki wielomianu: ",given_var)
    print("Maksymalna wartość w przedziale(",x_start,",",x_end,"):",max_val)
    print("Minimalna wartość w przedziale(",x_start,",",x_end,"):",min_val,"\n")
    plt.plot(interval, all_values)
    plt.scatter(*min_point, color='red', zorder=10, label='Minimum')
    plt.scatter(*max_point, color='yellow', zorder=10, label = 'Maksimum')
    plt.title("Wykres wartości wielomianu w podanym przedziale")
    plt.xlabel("x")
    plt.ylabel("Wartość wielomianu")
    plt.grid()
    plt.legend()
    plt.show()

#4.2


funkcja1()
funkcja2()
funkcja3(given_var = [-2,3,4], x_start = -10, x_end = 10, acc = 1000)

