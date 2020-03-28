# Whatsapp Chat Analyze

Este "proyecto"  surgió como la primera practica de mi aprendizaje en el lenguaje de python, el modelo y estructura de clases es bastante feo, todo surgió sobre la marcha, no era para nada un proyecto planeado.

#### ¿Cómo utilizar?
1. Exporta un chat de whatsapp
2. Mueve el fichero exportado a la carpeta "conversations"
3. Abre la consola y navega hasta la ruta donde está el script
4. Ejecuta Main.py
5. El script te pedirá el nombre del fichero, ingresarlo sin la extensión

Está considerado no contar el tiempo de respuesta para mensajes recibidos entre el bloque horario de 23 PM a 06 AM y que no posean una respuesta dentro 4 a 10 horas, ya que se asume que el sujeto estaba durmiendo.
(Se puede modificar el criterio en las constantes)


##### ¿Que información entrega?
1.  Total de mensajes enviados
2. Promedio de palabras escritas por cada mensaje
3. Tiempo de respuesta promedio del participante en minutos
4. total de palabras escritas en la conversación
5. Total de Mensajes multimedia enviados (Adjuntos, stickers, etc)


**El script está incompleto, tenia en mente obtener más datos curiosos como:**
- 3 Horas del dia donde un participante habla más
- 3 Dias de la semana donde un participante habla más 
- Sintetizar los datos y generar un porcentaje de interés
- Graficar el nivel de interés del participante a lo largo del tiempo 
