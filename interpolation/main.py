from functions import divided_diff
from functions import newton_poly
from functions import func
import numpy as np
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn-poster')

a = -6
b = 6
m = 40
arr_x = []
arr_f = []

for i in range(m):
    arr_x.append((a+b)*0.5 + (b-a)*math.cos(((2*(i+1)-1)/(2*m))*math.pi)*0.5)

for j in range(m):
    arr_f.append(func(arr_x[j]))

x = np.array(arr_x)
y = np.array(arr_f)
# get the divided difference coef
a_s = divided_diff(x, y)[0, :]

# evaluate on new data points
x_new = np.arange(-6, 6, .1)
y_new = newton_poly(a_s, x, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)

fun = [func(i) for i in arr_x]
plt.plot(arr_x, fun)
plt.show()