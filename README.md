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

# 3. Construcción y arquitectura del modelo

# 4. Entrenamiento del modelo

# 5. Exportación del modelo

# 6. Predicción


## Métricas
### Métrica F1

### Métrica Recall

### Métrica Precisión
Se utiliza la función `accuracy_score` de la librería de Keras, esta función sirve para comparar las clases verdaderas y las clases predichas y calcula la precisión del modelo en términos de la proporción de muestras clasificadas correctamente.



## Diagrama de arquitectura
![alt text](sentiment_analysis_RNA_LSTM/Diagrama%20Arq%20Modelo%20Sentiment.png)

## Diagrama de despliegue del API
![alt text](sentiment_analysis_RNA_LSTM/Diagrama%20Deploy%20API.png)