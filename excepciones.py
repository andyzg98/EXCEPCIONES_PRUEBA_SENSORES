import tkinter as tk

dispositivos_registrados = ["SNS100", "ACT200", "DIS003"]

def verificar_dispositivo(codigo):
    if codigo in dispositivos_registrados:
        return True
    else:
        return False

def mostrar_mensaje(mensaje):
    resultado_label.config(text=mensaje)

def verificar_dispositivo_controller():
    codigo = codigo_entry.get()
    try:
        if codigo.startswith("ACT"):
            raise Exception("¡Alerta! El dispositivo no está conectado")
        elif verificar_dispositivo(codigo):
            mostrar_mensaje("Dispositivo {}: Verificación exitosa. Funcionamiento normal".format(codigo))
        else:
            mostrar_mensaje("Error: código de dispositivo inválido")
    except Exception as e:
        mostrar_mensaje(str(e))
    
    # Borrar el contenido del cuadro de texto después de la verificación
    codigo_entry.delete(0, tk.END)

def agregar_sensor():
    nuevo_sensor = nuevo_sensor_entry.get()
    dispositivos_registrados.append(nuevo_sensor)
    mostrar_mensaje("Sensor {} agregado correctamente.".format(nuevo_sensor))
    
    # Borrar el contenido del cuadro de texto después de agregar el sensor
    nuevo_sensor_entry.delete(0, tk.END)

def eliminar_sensor():
    sensor_eliminar = eliminar_sensor_entry.get()
    if sensor_eliminar in dispositivos_registrados:
        dispositivos_registrados.remove(sensor_eliminar)
        mostrar_mensaje("Sensor {} eliminado correctamente.".format(sensor_eliminar))
    else:
        mostrar_mensaje("Sensor {} no encontrado.".format(sensor_eliminar))
    
    # Borrar el contenido del cuadro de texto después de eliminar el sensor
    eliminar_sensor_entry.delete(0, tk.END)

# Crear la ventana principal
window = tk.Tk()
window.title("Verificación de Dispositivos")

# Etiqueta y campo de entrada para el código del dispositivo
codigo_label = tk.Label(window, text="Código del dispositivo:")
codigo_label.pack()
codigo_entry = tk.Entry(window)
codigo_entry.pack()

# Botón para verificar el dispositivo
verificar_button = tk.Button(window, text="Verificar", command=verificar_dispositivo_controller)
verificar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(window, text="")
resultado_label.pack()

# Agregar Sensores Nuevos
nuevo_sensor_label = tk.Label(window, text="Nuevo sensor:")
nuevo_sensor_label.pack()
nuevo_sensor_entry = tk.Entry(window)
nuevo_sensor_entry.pack()
agregar_sensor_button = tk.Button(window, text="Agregar Sensor Nuevo", command=agregar_sensor)
agregar_sensor_button.pack()

# Eliminar Sensores
eliminar_sensor_label = tk.Label(window, text="Sensor a eliminar:")
eliminar_sensor_label.pack()
eliminar_sensor_entry = tk.Entry(window)
eliminar_sensor_entry.pack()
eliminar_sensor_button = tk.Button(window, text="Eliminar Sensor", command=eliminar_sensor)
eliminar_sensor_button.pack()

# Ejecutar la ventana principal
window.mainloop()
