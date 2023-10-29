from tkinter import *
from tkinter import messagebox
from datos import Database

datos = Database('ventas.db')

def populate_list():
    Producto_list.delete(0, END)
    for row in datos.fetch():
        Producto_list.insert(END, row)

def add_item():
    if producto_text.get() == '' or cliente_text.get() == '' or vendedor_text.get() == '' or precio_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    datos.insert(producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get())
    Producto_list.delete(0, END)
    Producto_list.insert(END, (producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global select_item
        index = Producto_list.curselection() [0]
        select_item = Producto_list.get(index)

        producto_entry.delete(0, END)
        producto_entry.insert(END, select_item[1])
        cliente_entry.delete(0, END)
        cliente_entry.insert(END, select_item[2])
        vendedor_entry.delete(0, END)
        vendedor_entry.insert(END, select_item[3])
        precio_entry.delete(0, END)
        precio_entry.insert(END, select_item[4])
    except IndexError:
        pass

def remove_item():
    datos.remove(select_item[0])
    clear_text()
    populate_list()

def update_item():
    datos.update(select_item[0], producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get())
    populate_list()

def clear_text():
    producto_entry.delete(0, END)
    cliente_entry.delete(0, END)
    vendedor_entry.delete(0, END)
    precio_entry.delete(0, END)



app = Tk()

producto_text = StringVar()
producto_label = Label(app, text="Producto", font=("bold", 12))
producto_label.grid(row=0, column=0, sticky=W)
producto_entry = Entry(app, textvariable=producto_text)
producto_entry.grid(row=0, column=1)

cliente_text = StringVar()
cliente_label = Label(app, text="cliente", font=("bold", 12))
cliente_label.grid(row=0, column=2, sticky=W)
cliente_entry = Entry(app, textvariable=cliente_text)
cliente_entry.grid(row=0, column=3)

vendedor_text = StringVar()
vendedor_label = Label(app, text="Vendedor", font=("bold", 12))
vendedor_label.grid(row=1, column=0, sticky=W)
vendedor_entry = Entry(app, textvariable=vendedor_text)
vendedor_entry.grid(row=1, column=1)

precio_text = StringVar()
precio_label = Label(app, text="Precio", font=("bold", 12))
precio_label.grid(row=1, column=2, sticky=W)
precio_entry = Entry(app, textvariable=precio_text)
precio_entry.grid(row=1, column=3)

Producto_list = Listbox(app, height=8, width=50, border=0)
Producto_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

Producto_list.bind('<<ListboxSelect>>', select_item)

btn1 = Button(app, text="Listar productos", width=12, command=add_item)
btn1.grid(row=2, column=0,pady=20)

btn2 = Button(app, text="Crear productos", width=12, command=add_item)
btn2.grid(row=2, column=1)

btn3 = Button(app, text="Actualizar productos", width=16, command=update_item)
btn3.grid(row=2, column=2)

btn4 = Button(app, text="Editar producto", width=14, command=add_item)
btn4.grid(row=2, column=3)

btn5 = Button(app, text="Eliminar producto", width=13, command=remove_item)
btn5.grid(row=2, column=4)



app.title("sistema de Transaccionales de ventas")
app.geometry("700x350")
populate_list()

app.mainloop()

