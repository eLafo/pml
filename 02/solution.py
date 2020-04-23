import numpy as np
import os
import linear_regression

X, Y = np.loadtxt("%s/pizza.txt" % os.path.dirname(os.path.realpath(__file__)), skiprows=1, unpack=True)
w, b = linear_regression.train(X, Y, iterations=10000, lr=0.01)
print("\nw=%3f, b=%3f" % (w, b))
print("Prediction: x=%d => y=%.2f" % (20, linear_regression.predict(20, w, b)))

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.plot(X, Y, "bo")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Reservations", fontsize=30)
plt.ylabel("Pizzas", fontsize=30)
x_edge, y_edge = 50, 50
plt.axis([0, x_edge, 0, y_edge])
plt.plot([0, x_edge], [b, linear_regression.predict(x_edge, w, b)], linewidth=1.0, color="g")
plt.show()
