from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

cancer = load_breast_cancer()

print("cancer.", list(cancer.keys()))

print("Description :")
print(cancer.DESCR)

print("Les noms des features : ", cancer.feature_names)
print("Il y a %s échantillons." % cancer.data.shape[0])
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=314)

print("Utilisation de l'algorithme K Nearest Neighbors (k = 1)")
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

print("La précision du modèle sur les données de test est de : ", knn.score(X_test, y_test))

print("Utilisation de l'algorithme K Nearest Neighbors (k = 5)")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

print("La précision du modèle sur les données de test est de : ", knn.score(X_test, y_test))

print("nice")
