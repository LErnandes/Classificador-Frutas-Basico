from sklearn import *

dados = [[140, 1], [130, 1], [150, 0], [170, 0], [300, 1], [500, 1]] # peso em gramas e superfície 1 - lisa 0 - irregular
frutas = [0, 0, 1, 1, 2, 2] # 0 Maça 1 Laranja 2 Melancia ()

tff = tree.DecisionTreeClassifier()
tff = tff.fit(dados, frutas)

print(tff.predict([[400, 1]]))
