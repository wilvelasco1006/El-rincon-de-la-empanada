import sqlite3
from programa.compras import principal
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

# Conectarse a la base de datos (creará un archivo de base de datos si no existe)
conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

# Crear la tabla de usuarios (si no existe)
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    nombre_usuario TEXT,
                    contraseña TEXT
                )''')



# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre_usuario = simpledialog.askstring('Usuario',"Ingresa tu nombre de usuario: ")
    contraseña = simpledialog.askstring('Contraseña',"Ingresa tu contraseña: ")

    # Insertar los datos del usuario en la base de datos
    cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre_usuario, contraseña))
    conexion.commit()
    messagebox.showinfo(message="\nUsuario registrado exitosamente.",title='Registro exitoso')


# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = simpledialog.askstring('Nombre Usuario',"\nIngresa tu nombre de usuario: ")
    contraseña = simpledialog.askstring('Contraseña',"Ingresa tu contraseña: ")

    # Verificar si los datos de inicio de sesión son válidos
    cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario=? AND contraseña=?", (nombre_usuario, contraseña))
    resultado = cursor.fetchone()

    if nombre_usuario == 'admin_user' and contraseña == '12345':
        admin = True
        messagebox.showinfo(message='Hola admin',title='Hola Admin')
    else:
        admin = False

    if resultado is not None:  # Verificar si hay un resultado válido
        messagebox.showinfo(message="Inicio de sesión exitoso.",title='Inicio Sesion')
        principal(ventana)
    else:
        messagebox.showinfo(message="Nombre de usuario o contraseña incorrectos.",title='Eror')



    
# Menú principal

def salir():
    messagebox.showinfo(message='Muchas Gracias, Vuelva pronto',title='Gracias')
    ventana.destroy()



ventana = Tk()
ventana.title('EL RINCON DE LA EMPANADA')
ventana.geometry('600x270')
ventana.config(bg='#FF8C00')


marcoSalidas = Frame(ventana)
marcoSalidas.config(width=100, height= 80, bd=  3, relief = "groove")
marcoSalidas.pack(pady = 10, padx = 10)
marcoSalidas.config(bg='#FFD700')

e1 = Label (marcoSalidas,text='EL RINCON DE LA EMPANADA',font=('Arial',18))
e1.config(bg= '#FFD700')
e1.pack(pady=10)

boton1= Button(marcoSalidas,text='REGISTARSE',command=registrar_usuario)
boton1.config(bg = "white")
boton1.pack(pady=10,padx=10)

boton2= Button(marcoSalidas,text='INICIAR SESION',command=iniciar_sesion)
boton2.config(bg = "white")
boton2.pack(pady=10,padx=10)

boton3= Button(marcoSalidas,text='SALIR',command=salir)
boton3.config(bg = "white")
boton3.pack(pady=10,padx=10)

ventana.mainloop()
conexion.close()
