# -*- coding: utf-8 -*-
"""Aula-Biblioteca-SciKit-Learn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zp_0LVcKZ8MfCAc9iAr5mWv-E-55wZTq
"""

from sklearn.datasets import make_regression

#GERANDO UMA MASSA DE DADOS
x, y = make_regression(n_samples=200, n_features=1, noise=30)

import matplotlib.pyplot as plt

#MOSTRANDO NO GRAFICO
plt.scatter(x,y)
plt.show()

from sklearn.linear_model import LinearRegression

#CRIAÇÃO DO MODELO
modelo = LinearRegression()
modelo.fit(x,y)

modelo.predict(x)

plt.scatter(x,y)
plt.plot(x, modelo.predict(x), color = "red", linewidth = 3)
plt.show()
