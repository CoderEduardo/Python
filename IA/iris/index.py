# =========================
# PROJETO: Rede Neural Iris
# =========================

# 1) IMPORTS
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical

# 2) CARREGAR E EXPLORAR DADOS
dados = load_iris()
X = dados.data                # shape: (150, 4) -> 150 amostras, 4 atributos
y = dados.target              # classes: 0, 1, 2 (setosa, versicolor, virginica)
nomes_classes = dados.target_names

print("Formato de X:", X.shape)
print("Exemplo de primeira linha de X:", X[0])
print("Valores de y (classes numéricas):", np.unique(y), "→", nomes_classes)

# 3) ONE-HOT ENCODING DO ALVO
# y: [0,1,2]  →  y_cat: [[1,0,0],[0,1,0],[0,0,1], ...]
y_cat = to_categorical(y, num_classes=3)

# 4) TREINO/TESTE (mantendo parte dos dados para avaliação honesta)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_cat, test_size=0.3, random_state=42, stratify=y
)

# 5) NORMALIZAÇÃO (ajuda muito redes neurais)
# Ajusta o scaler apenas no treino e aplica no treino e no teste
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# 6) DEFINIR A ARQUITETURA DA REDE
modelo = Sequential([
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)),  # 4 → 16
    Dropout(0.1),                                                   # ajuda a evitar overfitting
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')                                  # 3 classes (probabilidades)
])

# 7) COMPILAR O MODELO (otimizador, função de perda e métrica)
modelo.compile(optimizer='adam',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

# 8) CALLBACKS (parar cedo se não estiver melhorando)
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=15,          # quantas épocas sem melhorar até parar
    restore_best_weights=True
)

# 9) TREINAR (salvamos o histórico para plotar depois)
historico = modelo.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=200,
    batch_size=8,
    callbacks=[early_stop],
    verbose=0             # mude para 1 se quiser ver o log a cada época
)

# 10) AVALIAR NO CONJUNTO DE TESTE
loss, acc = modelo.evaluate(X_test, y_test, verbose=0)
print(f"\nDesempenho no teste → loss: {loss:.4f} | accuracy: {acc:.4f}")

# 11) RELATÓRIO DETALHADO
y_pred_prob = modelo.predict(X_test)
y_pred = np.argmax(y_pred_prob, axis=1)
y_true = np.argmax(y_test, axis=1)

print("\nRelatório de Classificação (por classe):")
print(classification_report(y_true, y_pred, target_names=nomes_classes))

print("Matriz de Confusão:")
print(confusion_matrix(y_true, y_pred))

# 12) CURVAS DE APRENDIZADO (loss e accuracy)
plt.figure(figsize=(12,5))

# Perda
plt.subplot(1,2,1)
plt.plot(historico.history['loss'], label='Treino')
plt.plot(historico.history['val_loss'], label='Validação')
plt.xlabel('Época')
plt.ylabel('Loss')
plt.title('Evolução da Perda')
plt.legend()

# Acurácia
plt.subplot(1,2,2)
plt.plot(historico.history['accuracy'], label='Treino')
plt.plot(historico.history['val_accuracy'], label='Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.title('Evolução da Acurácia')
plt.legend()

plt.tight_layout()
plt.show()

# 13) FUNÇÃO DE PREVISÃO PARA NOVOS DADOS
def prever_flor(sepal_length, sepal_width, petal_length, petal_width):
    # monta vetor, aplica mesmo scaler e prediz
    vetor = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    vetor_scaled = scaler.transform(vetor)
    probas = modelo.predict(vetor_scaled)
    classe_idx = np.argmax(probas, axis=1)[0]
    classe_nome = nomes_classes[classe_idx]
    return classe_nome, probas[0]

# Exemplo rápido:
ex_classe, ex_probas = prever_flor(5.1, 3.5, 1.4, 0.2)
print("\nExemplo de previsão para [5.1, 3.5, 1.4, 0.2]:")
print("Classe prevista:", ex_classe)
print("Probabilidades:", ex_probas)
