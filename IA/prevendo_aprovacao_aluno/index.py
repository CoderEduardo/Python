import pandas as pd

# Criando um dicionário com os dados
dados = {
    "nota": [8, 5, 7, 6, 4, 9, 3, 10, 2, 6.5],  # notas dos alunos
    "presenca": [90, 80, 85, 95, 70, 100, 60, 100, 50, 90],  # presença em %
    "resultado": ["Aprovado", "Reprovado", "Aprovado", "Aprovado", "Reprovado",
                  "Aprovado", "Reprovado", "Aprovado", "Reprovado", "Aprovado"]  # alvo
}

# Transformando em DataFrame
df = pd.DataFrame(dados)

# Mostrar os dados
print(df)

# Separando features e target
X = df[["nota", "presenca"]]  # características
y = df["resultado"]  # alvo

from sklearn.model_selection import train_test_split

#dividir dados: 80% treino 20% teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.neighbors import KNeighborsClassifier

#criando o modelo
modelo = KNeighborsClassifier(n_neighbors=3)

#treinar o modelo
modelo.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar a acurácia
print("Acurácia do modelo:", accuracy_score(y_test, y_pred))

# Entradas do usuário
nota_nova = float(input("Digite a nota do aluno: "))
presenca_nova = float(input("Digite a presença do aluno (%): "))

# Fazer a previsão
previsao = modelo.predict([[nota_nova, presenca_nova]])
print(f"O aluno provavelmente será: {previsao[0]}")

