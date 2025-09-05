import warnings
warnings.filterwarnings("ignore")            # ocultar warnings generales
import tensorflow as tf
tf.get_logger().setLevel('ERROR')            # ocultar logs de TF
import matplotlib.pyplot as plt
import numpy as np

# Datos de entrenamiento
celsius = np.array([-40, -10, 0, 8, 15, 22, 38, 40, 1875, 4736], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100, 104, 3407, 8556.8], dtype=float)

# Definición del modelo usando Input layer recomendado
modelo = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(12, activation='relu'),
    tf.keras.layers.Dense(12, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compilación
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# Lista para almacenar la pérdida por época
historial_loss = []

# Callback para capturar la pérdida en cada época
class LossHistory(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        historial_loss.append(logs['loss'])
        if (epoch + 1) % 50 == 0:  # mostrar cada 50 épocas
            print(f"Época {epoch+1}: Loss={logs['loss']:.4f}")

# Entrenamiento
print("\n[!] Comenzando entrenamiento...")
modelo.fit(celsius, fahrenheit, epochs=600, verbose=0, callbacks=[LossHistory()])
print("[+] Modelo entrenado!")

# Gráfica de pérdida
plt.figure(figsize=(10,5))
plt.plot(historial_loss, label="Loss (MSE)")
plt.title("Evolución de la pérdida durante el entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Loss")
plt.legend()
plt.show()

# Función para predecir
def predecir_celsius_a_fahrenheit(valor_celsius):
    return modelo.predict(np.array([valor_celsius]))[0][0]

# Loop interactivo
while True:
    try:
        grado_celsius = float(input("\n[+] Ingresa el grado Celsius para convertir a Fahrenheit: "))
        resultado_fahrenheit = predecir_celsius_a_fahrenheit(grado_celsius)
        print(f"[+] El resultado es {resultado_fahrenheit:.2f} Fahrenheit.")
    except KeyboardInterrupt:
        print("\n[!] Saliendo del programa...")
        break
    except ValueError:
        print("[!] Por favor ingresa un número válido.")
