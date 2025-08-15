import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Carregar o dataset
dados = load_iris()
X = dados.data
y = dados.target.reshape(-1, 1)

# 2. One-hot encoding
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# 3. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# 4. Criar o modelo
modelo = Sequential()
modelo.add(Dense(8, input_shape=(4,), activation='relu'))
modelo.add(Dense(8, activation='relu'))
modelo.add(Dense(3, activation='softmax'))

# 5. Compilar
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 6. Treinar e salvar histórico
historico = modelo.fit(X_train, y_train, epochs=100, verbose=0, validation_data=(X_test, y_test))

# 7. Avaliar no teste
loss, acc = modelo.evaluate(X_test, y_test)
print(f"\nAcurácia final: {acc:.4f}")

# 8. Plotar gráficos
plt.figure(figsize=(12,5))

# Gráfico da perda
plt.subplot(1, 2, 1)
plt.plot(historico.history['loss'], label='Treino')
plt.plot(historico.history['val_loss'], label='Validação')
plt.xlabel('Época')
plt.ylabel('Loss')
plt.title('Evolução da Perda')
plt.legend()

# Gráfico da acurácia
plt.subplot(1, 2, 2)
plt.plot(historico.history['accuracy'], label='Treino')
plt.plot(historico.history['val_accuracy'], label='Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.title('Evolução da Acurácia')
plt.legend()

plt.show()
