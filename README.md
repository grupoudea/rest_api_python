# Text Sentiment Analysis Clasification

Se implementa un modelo de entrenamiento de lenguaje natural para la clasificación de analisis de sentimientos. Este modelo será capaz de procesar y comprender el texto en diferentes contextos y clasificarlo en categorías como positivo, negativo o neutral. 
Para entrenar el modelo se utiliza la red neuronal LSTM. Durante el proceso de entrenamiento, ajustaremos los parámetros de la red LSTM utilizando técnicas de optimización y retropropagación del error para minimizar la función de pérdida y mejorar el rendimiento del modelo.

## Twitter Dataset

Este dataset es un conjunto de datos para el análisis de sentimientos a nivel de entidad en Twitter. La tarea consiste en, dado un mensaje y una entidad, evaluar el sentimiento del mensaje hacia la entidad. Hay tres clases en este conjunto de datos: **Positive**, **Negative** y **Neutral**. Consideramos que los mensajes que no son relevantes para la entidad (es decir, **Irrelevant**) son Neutrales.
Se utiliza un dataset de **74.682** registros de sentimientos. El dataset es un archivo CSV que se compone de 4 columnas.

 - **Tweet ID**: *Columna 1*.  Contiene un identificador único para cada tweet.
 - **Entity**: *Columna 2*. Indica la entidad específica mencionada en el tweet. Puede ser una marca, una persona, un producto, un evento u otro tipo de entidad a la que se refiere el mensaje.
 - **Sentiment**: *Columna 3*. Muestra la clasificación de sentimiento asociada al tweet. Puede haber varias categorías de sentimiento, como **positivo**, **negativo** o **neutral**. Esta clasificación indica la actitud general expresada en el tweet hacia la entidad mencionada.
 - **Tweet content**: *Columna 4*. Contiene el texto completo del tweet en sí. Aquí es donde se encuentra el contenido real del mensaje publicado en Twitter. Este texto es el que se analizará para determinar el sentimiento hacia la entidad mencionada.


# 1. Limpiar los datos

Se realiza una limpieza de los datos para eliminar los ruidos que podrían contener algunos tweets, palabras que son irrelevantes pueden afectar la presición de predicción. 

 - Se intenta eliminar las palabras y tweets que contengan emoticonos y caracteres especiales. 
 - Se remueven del dataset tweets que sean de la clase Irrelevant.
 - Se remueven del dataset tweets que contengan una sola palabra en el contenido.
 - Se normalizan los tweets para que todas las palabras sean en minúscula.

# 2. Vectorización de los datos
Se divide el texto en unidades más pequeñas llamadas tokens, se logra representar el texto de manera numérica, lo que facilita su procesamiento y análisis para asignar un identificador numérico a cada token, de la siguiente manera:

```python
    tokens = tokenizer.texts_to_sequences(twt)
    tokens_padded = pad_sequences(tokens, maxlen=166)
```
 
Este paso es fundamental ya que permite trabajar con texto de manera eficiente, al proporcionar una representación numérica, reducir la dimensionalidad y revelar información lingüística importante.

# 3. Construcción y arquitectura del modelo

Se tiene un modelo de red neuronal (LSTM) para analisis de sentimientos.

La construcción del modelo es la siguiente:

```python
embed_dim = 128
lstm_out = 196

model = Sequential()
model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(3,activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())
```

En las siguientes línea se tiene un dimensión de embeddings (dimesión vectorial en las que se representan las palabras del modelo) de 128 y el número de unidades LSTM = 196.

```python
embed_dim = 128
lstm_out = 196
```

Se crea un modelo secuencial con una capa de embedding, esta capa mapea los indices enteros de las palabras a vectores de embeddings de tamaño *embed_dim*. La variable *max_fatures* representa el tamaño del vocabulario (el número maximo de palabras distintas a considerar).

Se agrega una capa de dropout espacial de 1D **(SpatialDropout1D)**. Esto aplica a las salidas de la capa embedding, lo que ayuda a evitar el sobreajueste, ya que apaga aleatoriamente algunas unidades durante el entrenamiento. 

```python
model = Sequential()
model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
model.add(SpatialDropout1D(0.4))
```
Se agrega la capa LSTM al modelo con *lstm_uot* unidades LSTM. EL dropout y recurrente dropout, de acuerdo a la documentación en keras consideran valores entre 0 y 1 y especifican la tasa dropout para las conexiones entre las celdas LSTM y para las conexiones recurrentes.

Finalmente para la capa de salida, se agrega una capa densa con tres unidades y una función de activación softmax. Esta capa representa las probabilidades de pertenercer a cada unas de las 3 clases de sentimiento (positive, negative, neutral).

El modelo se compila con una función de pérdida categorical_crossentropy, el optimizador adam y las metricas a utilizar durante el entrenamiento, precisión. 

En la ultima linea, se imprime el resumen del modelo, donde se muestra la arquitectura y el número de parámetros entrenables. 

```python
model.add(Dense(3,activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())
```
## arquitectura del modelo

![alt text](sentiment_analysis_RNA_LSTM/lstm-rnn.png)

1. Capa embedding: esta capa convierte los indices de las palabras en vectores de embeddings de tamaño *embed_dim*. Se usa la variable *max_fatures* que representa el tamaño del vocabulario (el número maximo de palabras distintas a considerar).

2. Capa dropout: Esta capa aplica el dropout a las salidas de la capa de embedding. Su función es regularizar y evitar el sobreajuste.

3. Capa LSTM: Esta capa está compuesta por un total 196 unidades LSTM (lstm_out) y es responsable de procesar y aprender las sencuencias de entrada para capturar patrones temporales en los datos.

4. Capa densa: Es la capa de salida, consta de 3 neuronas. Esta capa produce salidas clasificadas apoyandose en en las capas anteriores. 



# 4. Entrenamiento del modelo

```python
Y = dataset_train[:, 0]
Y1 = pd.get_dummies(dataset_train[:, 0]).values

X_train, X_test, Y_train, Y_test = train_test_split(X,Y1, test_size = 0.33, random_state = 42)

inicio = datetime.datetime.now()
print('Inicia: ', inicio)

batch_size = 35
model.fit(X_train, Y_train, epochs = 15, batch_size=batch_size, verbose = 2)

fin  = datetime.datetime.now()
print('Termina: ', fin)
print('Duracion: ', fin - inicio)
```

Cómo primer paso se realiza una obtención de los valores de la variable de salida (las etiquetas). Se hace uso de la función get_dummies par obtener los valores como one-hot-enconding. 

Para entrar el modelo se opta por usar la función **train_test_split** que permite dividir de manera aleatoria un conjunto de datos en conjuntos de entrenamiento y prueba. En este caso se toma el 33% del conjunto de datos que se usará como conjunto de pruebas. 

```python
model.fit(X_train, Y_train, epochs = 15, batch_size=batch_size, verbose = 2)
```

Con la línea anterior se entrena el modelo haciendo uso de 15 epocas y un batch size de 35, lo que significa que se actualizan los pesos con mayor frecuencia. 

```python
validation_size = 1500

X_validate = X_test[-validation_size:]
Y_validate = Y_test[-validation_size:]
X_test = X_test[:-validation_size]
Y_test = Y_test[:-validation_size]
score,acc = model.evaluate(X_test, Y_test, verbose = 2, batch_size = batch_size)
print("score: %.2f" % (score))
print("acc: %.2f" % (acc))
```

Con las líneas anteriores se evalua el modelo donde al final se obtiene el puntaje y la precisión del mismo. Para evaluarlo se toman y remueven 1500 muetras del conjunto de pruebas y se le pasan a la función **evaluate**. 
La puntuación o score obtenida está entre **0.5 y 0.6**, mientras que la precisión está entre **0.82 y 0.87** en diferentes configuraciones que se la realizaron a la construcción del modelo.


# 5. Exportación del modelo
Mediante la función "model.save()" que se utiliza para guardar modelos en varias bibliotecas de aprendizaje automática como TensorFlow o Keras.

La función "save" toma dos argumentos principales: "ruta_guardado" y "save_format". "ruta_guardado" es la ubicación y el nombre de archivo donde se guardará el modelo. Puedes especificar la ruta completa junto con el nombre del archivo o solo el nombre del archivo si deseas guardarlo en el directorio actual.

El segundo argumento, "save_format", especifica el formato en el que se guarda el modelo. En este caso, se utiliza 'h5', que es una abreviatura de Hierarchical Data Format versión 5. 

Ventajas: 

- Al exportar un modelo, puedes guardarlo en un archivo y utilizarlo más tarde sin tener que volver a entrenarlo desde cero.
- Permite integrarlo fácilmente en las aplicaciones y utilizarlo para hacer predicciones en tiempo real.


# 6. Predicción usando REST API

Para usar el modelo y realizar prediciones con algunos comentarios de twitter, se expone el modelo a través de una REST API construida en Python usando Flask.

Está API es sencilla y cumple con ciertas tareas para lograr usar el modelo exportado como .h5. Algunas de estpas tareas:

- Limpiar el comentario que se envía desde el frontend
- Tokenizar el comentario para poder enviar al modelo dicha representación
- Cargar el modelo exportado en .h5 usando keras.
- Validar resultado del modelo
- retornar objeto con la información necesaria para determinar el sentimiento (clasificación) en el frontend




## Métricas
### Métrica F1
Se utiliza la función `f1_score` El F1 es una métrica que combina tanto la precisión como el recall en una sola medida. Esto es práctico porque hace más fácil el poder comparar el rendimiento combinado de la precisión y el recall entre varias soluciones.

### Métrica Recall
Se utiliza la función `recall_score` El Recall (también conocido como sensibilidad) es una métrica que mide la capacidad de un modelo para encontrar todos los ejemplos positivos en un conjunto de datos. En otras palabras, indica la proporción de ejemplos positivos que el modelo ha identificado correctamente.

### Métrica Precisión
Se utiliza la función `accuracy_score` de la librería de Keras, esta función sirve para comparar las clases verdaderas y las clases predichas y calcula la precisión del modelo en términos de la proporción de muestras clasificadas correctamente.



## Diagrama de arquitectura
![alt text](sentiment_analysis_RNA_LSTM/Diagrama%20Arq%20Modelo%20Sentiment.png)

## Diagrama de despliegue del API
![alt text](sentiment_analysis_RNA_LSTM/Diagrama%20Deploy%20API.png)
