# 🥟 El Rincón de la Empanada

Este proyecto es una aplicación de escritorio desarrollada en Python con `tkinter` para gestionar pedidos de un restaurante llamado **"El Rincón de la Empanada"**. La aplicación permite a los usuarios registrarse, iniciar sesión y realizar pedidos de productos como empanadas, papas rellenas, aborrajados y marranitas.

---

## 🚀 Funcionalidades

### 1. 🔐 Registro e Inicio de Sesión
- 👤 Los usuarios pueden registrarse con un nombre de usuario y contraseña.
- 🗄️ Los datos de los usuarios se almacenan en una base de datos SQLite (`usuarios.db`).
- ✅ Los usuarios pueden iniciar sesión para acceder a las funcionalidades de pedidos.
- 🛠️ Existe un usuario administrador (`admin_user` con contraseña `12345`) que tiene privilegios especiales.

### 2. 🛒 Gestión de Pedidos
- 🗺️ Los usuarios pueden seleccionar una sucursal (Norte, Sur, Este, Oeste).
- 🍽️ Pueden elegir productos del menú y especificar la cantidad deseada.
- 💰 Se calcula el total a pagar, incluyendo un costo de domicilio fijo.
- 📦 Los usuarios proporcionan su dirección, método de pago y número de contacto.

### 3. 🖥️ Interfaz Gráfica
- 🧱 La aplicación utiliza `tkinter` para crear una interfaz gráfica amigable.
- 💬 Incluye cuadros de diálogo (`messagebox`, `simpledialog`) para interactuar con el usuario.

---

## 📁 Archivos del Proyecto

- `programa/compras.py`: Contiene la lógica para gestionar los pedidos.
- `programa/login terminado.py`: Contiene la lógica para el registro e inicio de sesión de usuarios.
- `usuarios.db`: Base de datos SQLite para almacenar los datos de los usuarios (se genera automáticamente si no existe).
- `README.md`: Archivo descriptivo del proyecto.

---

## 🧰 Requisitos

- Python 3.x
- Librerías estándar: `tkinter`, `sqlite3`

---

## ▶️ Cómo Ejecutar

1. 📥 Clona este repositorio en tu máquina local.
2. 🐍 Asegúrate de tener Python 3.x instalado.
3. 💻 Ejecuta el archivo `login terminado.py` para iniciar la aplicación:

```bash
python programa/login\ terminado.py
