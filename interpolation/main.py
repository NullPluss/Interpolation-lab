from functions import divided_diff
from functions import newton_poly
from functions import func
import numpy as np
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn-poster')

a = -3
b = 3
n = 5
arr_x = []
arr_f = []

for i in range(1, n+1):
    arr_x.append((a+b)*0.5 + (b-a)*math.cos(((2*i-1)/n)*math.pi)*0.5)

for j in range(n):
    arr_f.append(func(arr_x[j]))

x = np.array(arr_x)
y = np.array(arr_f)
# get the divided difference coef
a_s = divided_diff(x, y)[0, :]

# evaluate on new data points
x_new = np.arange(-4, 4, .1)
y_new = newton_poly(a_s, x, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)
plt.axis((-4, 4, -4, 4))
plt.show()