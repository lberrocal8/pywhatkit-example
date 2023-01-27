# Python-pywhatkit
 Envio de mensajes a WhatsApp con Python y pywhatkit.

En el directorio podrás encontrar 3 archivos:
1. bd_contactos.txt: En este archivo solo vas a escribir un número de teléfono, por linea. No necesitas agregar el código de área de tu país (los números de teléfono no deben tener espacios entre sí, guiones o puntos).
2. mensaje.txt: En este archivo vas a escribir el mensaje que quieres envíar. Acepta mensajes multilinea, acentos y emojis.
3. pywhatkit_send.py: En este archivo esta el código de ejecución del script. Ten en cuenta que, dependiendo de tu país y/o del país de los destinatarios, así debes modificar la linea 6, modificar el '+57' por el indicativo de tu país y/o el del destinatario.

Ádemas ten en cuenta que si no tienes instalada la libreria de pywhatkit, debes hacerlo con la siguiente instrucción:
pip install pywhatkit

Támbien debes tener en cuenta que debes tener abierta una sesión de WhatsApp Web en el computador donde ejecutas el código.

## Funcionamiento
1. Se abre el archivo bd_contactos.txt, en segundo plano, para extraer los números de teléfono.
2. Se abre, el archivo mensaje.txt, en segundo plano, para extraer el mensaje a enviar.
3. Se recorre el archivo bd_contactos.txt para enviar a cada número, el mensaje.
4. Por cada número, el script abre la sesión de whatsapp, envía el mensaje y luego cierra la pestaña. Esto se repite como tantos números existan en el archivo bd_contactos.txt.
5. Se cierran los archivos abiertos.

El script muestra por consola a que números se esta enviando el mensaje y a que número no se pudo envíar.
