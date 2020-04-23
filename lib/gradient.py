import numpy as np 
import linear_regression

def gradient_without_bias(X, Y, w):
  return 2 * np.average(X * (linear_regression.predict(X, w, 0) - Y))

def train(X, Y, iterations, lr):
  w = 0
  for i in range(iterations):
    print("Iteration %4d => Loss: %.10f" % (i, linear_regression.loss(X, Y, w, 0)))
    w -= gradient_without_bias(X, Y, w) * lr
  return w
# X, Y = np.loadtxt("data/pizza.txt", skiprows=1, unpack=True)
# w = train(X, Y, iterations=100, lr=0.001)