import pywhatkit as wa

with open('bd_contactos.txt', 'r') as contactos:
    for numero in contactos:
        with open('mensaje.txt', 'r', encoding='UTF-8') as mensaje:
            numero = "+57" + numero
            try:
                wa.sendwhatmsg_instantly(numero, mensaje.read(), 10, True)
                print("Mensaje enviado")
            except:
                print("Error al enviar el mensaje: " + numero)
        mensaje.close()
        