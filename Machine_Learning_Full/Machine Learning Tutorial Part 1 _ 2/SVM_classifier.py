# Problem is to classify muffin and cupcakes recipes using support vector machines.



# import packages
import numpy as np
import pandas as pd
from sklearn import svm

import seaborn as sns
sns.set(style="ticks")
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})


recipes = pd.read_csv('/Users/aneupane/Desktop/python/Machine_Learning_Full/Machine Learning Tutorial Part 1 _ 2/Cupcakes vs Muffins.csv')
print(recipes.head())

sns.lmplot("Flour", "Sugar", data=recipes, hue='Type', fit_reg=False)
plt.show()


type_label = np.where(recipes['Type']=='Muffin', 0,1)
recipe_features = recipes.columns.values[1:].tolist()
ingredients = recipes[['Flour', 'Sugar']].values

# Fit model
model = svm.SVC(kernel = 'linear')
model.fit(ingredients, type_label)

# Get separating hyperplane
w = model.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(30,60)
yy = a * xx - (model.intercept_[0])/ w[1]

# Plot the parallels to the separating hyperplane that pass through the support
# vectors
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])

b = model.support_vectors_[-1]

yy_up = a * xx + (b[1] - a * b[0])

sns.lmplot('Flour', 'Sugar', data = recipes, hue = 'Type', palette = 'Set1', fit_reg = False, scatter_kws = {"s": 70})
plt.show()


X = np.random.uniform(size=100).reshape(50, 2)
y = np.dot(X, [[1, 2, 3], [3, 4, 5]])
