# On en profite aussi pour tester si mglearn marche bien
import mglearn
import matplotlib.pyplot as plt

# On fait le graphique de données plus ou moins bidons
# X, y = mglearn.datasets.make_forge()
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# Mdr en fait c'est juste une putain d'image statique c'est trop guez 🤣
mglearn.plots.plot_knn_classification(n_neighbors=1)
plt.show()
