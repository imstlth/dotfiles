from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris_dataset = load_iris()

print("Les classes (espèces) des iris :")
print(iris_dataset["target_names"])
print("Les features de chaque échantillon :")
print(iris_dataset["feature_names"])

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset["feature_names"])
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker="o", hist_kwds={"bins": 20}, s=60)
plt.show()

print("Nous allons utiliser l'algorithme k nearest neighbors (knn).")
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print("À quelle espèce appartient un iris ayant des sépales lxL 5x2,9 et des pétales 1x0,2 ?")
X_new = np.array([[5, 2.9, 1, 0.2]])
y_new_pred = knn.predict(X_new)
print("Selon le modèle, c'est un ", iris_dataset["target_names"][y_new_pred])

print("On calcule maintenant la précision du modèle à partir des données de test")
y_pred = knn.predict(X_test)
score = np.mean(y_pred == y_test)
# C'est égal à
score_knn = knn.score(X_test, y_test)
print("Il a un degrés de précision de ", score)
