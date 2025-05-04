from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
def principal(ventana):
    CanAborrajado = 0
    CanEmpanada = 0
    CanMarranitas = 0
    CanPapas = 0
    valorAborrajado = 0
    valorEmpanada = 0
    valorMarranita = 0
    valorPapa = 0
    sucursal = simpledialog.askstring('Bienvenido',"BIENVENIDO AL RINCON DE LA EMPANADA\n\nPor favor escoja una sucursal\nSucursal Norte, Sur, Este, Oeste: ").lower()
    while sucursal != 'norte' and sucursal != 'sur' and sucursal != 'este' and sucursal != 'oeste':
        mensaje = messagebox.showerror(message = 'por favor solo escriba una de las siguientes opciones: Sur/Norte/Este/Oeste.', title = 'Dato no valido' )
        sucursal = simpledialog.askstring('Bienvenido',"Sucursal Norte, Sur, Este, Oeste: ").lower()

        
    confirmacion = "si"
    while (confirmacion == "si"):   
        producto = simpledialog.askinteger('Opciones',"\nEscoja una de nuestras opciones\n\n1-Empanada\n2-Papa Rellena\n3-Aborrajado\n4-Marranita\n\n¿Que producto quiere?: ")
        while producto < 1 or producto > 4:
            mensaje = messagebox.showerror(message = 'Escoja un producto valido.', title = 'Error' )
            producto = simpledialog.askinteger('Opciones',"\nEscoja una de nuestras opciones\n\n1-Empanada\n2-Papa Rellena\n3-Aborrajado\n4-Marranita\n\n¿Que producto quiere?: ")

        if (producto == 1):
            CanEmpanada = simpledialog.askinteger('Cantidad',"¿Cuantas Empanadas quiere?: ")
            valorEmpanada = (CanEmpanada*1500)
                
        if (producto == 2):
            CanPapas = simpledialog.askinteger('Cantidad',"¿Cuantas papas rellenas quiere?: ")
            valorPapa = (CanPapas*3000)
                
        if (producto == 3):
            CanAborrajado = simpledialog.askinteger('Cantidad',"¿Cuantos aborrajados quiere?: ")
            valorAborrajado = (CanAborrajado*2500)
            
        if (producto == 4):
            CanMarranitas = simpledialog.askinteger('Cantidad',"¿Cuantas marranitas quiere?: ")
            valorMarranita = (CanMarranitas*3000)

            

        confirmacion = simpledialog.askstring('Otro?',"¿Quiere otro producto?: ").lower()
        while confirmacion != 'si' and confirmacion != 'no':
            confirmacion = simpledialog.askstring('Otro?','Por favor escoja una opcion valida: Si/No\n¿Quiere otro producto?: ').lower()
    
    direccion = simpledialog.askstring('Direccion',"\nDigite la dirección de entrega: ")
    MetodoPago = simpledialog.askinteger('Tipo de pago',"\nMetodo de pago\n\n1-Contraentrega\n2-Tajerta\n\nDigite el metodo de pago: ")
    while MetodoPago != 1 and MetodoPago != 2:
        MetodoPago = simpledialog.askinteger('Error',"Por favor escoja un metodo de pago valido\n\n1-Contraentrega\n2-Tajerta\n\nDigite el metodo de pago: ")

    
    if MetodoPago == 1:
        mPago = 'Contraentrega'
    elif MetodoPago == 2:
        mPago = 'Tarjeta'
    totalPagar = (valorAborrajado + valorEmpanada + valorMarranita + valorPapa)    
    celular = simpledialog.askinteger('Numero',"Digite su numero celular: ")
    x = "Recibo de pago:\nSucursal: "+str(sucursal)+'\nDireccion de pedido: '+str(direccion)+'\nMetodo de pago: '+str(mPago)+'\nCelular: '+str(celular)+'\nCantidad Empanadas: '+str(CanEmpanada)+'\nCantidad Papas Rellenas: '+str(CanPapas)+'\nCantidad Aborrajado: '+str(CanAborrajado)+'\nCantidad Marranita: '+str(CanMarranitas)+'\nTotal a Pagar: '+str(totalPagar)+'\nDomicilio: 5000'+'\nCuenta Total: '+str(totalPagar + 4000)
    messagebox.showinfo(message=x,title='Recibo')

    afuera = simpledialog.askinteger('Salida','Escribe 0 para salir:')
    if afuera == 0:
        messagebox.showinfo(message='Saliendo...',title='Salida')
        ventana.destroy()







