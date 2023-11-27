import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import ttk
from tkinter import messagebox
import pymongo
from pymongo import collection
import requests
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import cv2
from pyzbar.pyzbar import decode
import time
import threading
from PIL import ImageTk, Image


uri = "mongodb+srv://mongo:Miuniversidad2023@cluster0.sfa5efq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Verdana', size=16)
        self.geometry("400x750")
        self.title("ParticipoMX")
        self.configure(bg="black")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (Inicio, ConfirmarDatos, Votar, Gracias, ReconocimientoFacial):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.configure(bg="black")
            self.frames[page_name] = frame


            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("Inicio")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Inicio(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="1. Escanea el código QR \nbidimensional de tu INE", font=controller.title_font)
        label.pack(side="top", fill="x")

    def capturarQR():
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # Ancho del video
        cam.set(4, 480)  # Alto del video

        def leerQR():
            while True:
                success, frame = cam.read()

                for qr_code in decode(frame):
                    print(qr_code.type)
                    print(qr_code.data.decode('utf-8'))
                    time.sleep(6)

                cv2.imshow("QR_Scanner", frame)
                if cv2.waitKey(1) == ord('q'):
                    break

        t = threading.Thread(target=leerQR)
        t.start()

        def cerrarCamara():
            cam.release()
            cv2.destroyAllWindows()

        self.protocol("WM_DELETE_WINDOW", cerrarCamara)

    frame = tk.Frame(bg="gray", width=640, height=480)
    frame.pack(side="top", fill="x")

    canvas = tk.Canvas(frame, width=640, height=480)
    canvas.pack()

    def leerQR():
        while True:
            success, frame = cam.read()

            # Convertir el marco de OpenCV a una imagen de PIL
            imagen = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imagen = imagen.resize((640, 480), Image.ANTIALIAS)
            imagen = ImageTk.PhotoImage(imagen)

            # Actualizar el lienzo con la nueva imagen
            canvas.create_image(0, 0, anchor=tk.NW, image=imagen)
            canvas.image = imagen

            for qr_code in decode(frame):
                print(qr_code.type)
                print(qr_code.data.decode('utf-8'))
                time.sleep(6)

            if cv2.waitKey(1) == ord('q'):
                break

        cerrarCamara()


        button1 = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2,
                            padx=3, pady=3, font="Verdana", text=">>>", command=lambda:controller.show_frame("ReconocimientoFacial"))
        button1.pack()



class ReconocimientoFacial(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="Reconocimiento Facial", font=controller.title_font)
        label.pack(side="top", fill="x")


        frame = tk.Frame(self, bg="green", width=250, height=600)
        frame.pack(side="top", fill="x")


        button1 = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2,
                            padx=3, pady=3, font="Verdana", text=">>>", command=lambda: controller.show_frame("ConfirmarDatos"))
        button1.pack()




class ConfirmarDatos(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="Confirma tus datos", font=controller.title_font)
        label.pack(side="top", fill="x")

        input_vars = []


        # Crear 13 inputs de entrada de texto con etiquetas personalizadas
        etiquetas = ["ID", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "ID", "TELÉFONO", "HASH ACTUAL", "HASH PÚBLICO", "FIRMA", "HASH PREVIO", "VOTADO", "TIMESTAMP", "CLAVE ELECTOR", "ENTIDAD", "ESTADO", "SECCIÓN"]
        valores_predeterminados = ["", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", ""]


        for i, etiqueta in enumerate(etiquetas):
            label = tk.Label(self, foreground="White",
                             bg="black", text=etiqueta)
            label.pack()


            input_var = tk.StringVar()
            # Establecer contenido predeterminado
            input_var.set(valores_predeterminados[i])
            input_vars.append(input_var)


            entry = tk.Entry(self, textvariable=input_var)
            entry.pack()


        def check_inputs():
            for var in input_vars:
                if len(var.get()) == 0:
                    return False
            return True


        button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2, padx=3, pady=3,
                           font="Verdana", text="Continuar", command=lambda: controller.show_frame("Votar") if check_inputs() else None)
        button.pack()





def mostrarDatos(tabla, limit=1):
    try:
        cliente = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
        baseDatos = cliente["padron"]
        coleccion = baseDatos["padron1"]

        documentos = coleccion.find().limit(limit)

        for documento in documentos:
            datos = [
                documento["_id"],
                documento["nombre"],
                documento["apellido_paterno"],
                documento["apellido_materno"],
                documento["id"],
                documento["telefono"],
                documento["hash_actual"],
                documento["hash_publico"],
                documento["firma"],
                documento["hash_previo"],
                documento["votado"],
                documento["timestamp"],
                documento["clave_elector"],
                documento["entidad"],
                documento["estado"],
                documento["seccion"]
            ]
            tabla.insert('', 'end', values=datos)

        cliente.server_info()
        print("Consulta con la base de datos de Mongo exitosa")
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo excedido " + str(errorTiempo))
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a MongoDB " + str(errorConexion))



tabla = ttk.Treeview()
tabla.pack(fill="both", expand=True)
tabla["columns"] = ("ID", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "ID", "TELÉFONO", "HASH ACTUAL", "HASH PÚBLICO", "FIRMA", "HASH PREVIO", "VOTADO", "TIMESTAMP", "CLAVE ELECTOR", "ENTIDAD", "ESTADO", "SECCIÓN")
tabla.column("#0", width=50)
tabla.column("ID", width=100)
tabla.column("NOMBRE", width=100)
tabla.column("APELLIDO PATERNO", width=100)
tabla.column("APELLIDO MATERNO", width=100)
tabla.column("ID", width=50)
tabla.column("TELÉFONO", width=100)
tabla.column("HASH ACTUAL", width=100)
tabla.column("HASH PÚBLICO", width=100)
tabla.column("FIRMA", width=100)
tabla.column("HASH PREVIO", width=100)
tabla.column("VOTADO", width=50)
tabla.column("TIMESTAMP", width=100)
tabla.column("CLAVE ELECTOR", width=100)
tabla.column("ENTIDAD", width=100)
tabla.column("ESTADO", width=100)
tabla.column("SECCIÓN", width=100)
tabla.heading("#0", text="ID")
tabla.heading("ID", text="ID")
tabla.heading("NOMBRE", text="NOMBRE")
tabla.heading("APELLIDO PATERNO", text="APELLIDO PATERNO")
tabla.heading("APELLIDO MATERNO", text="APELLIDO MATERNO")
tabla.heading("ID", text="ID")
tabla.heading("TELÉFONO", text="TELÉFONO")
tabla.heading("HASH ACTUAL", text="HASH ACTUAL")
tabla.heading("HASH PÚBLICO", text="HASH PÚBLICO")
tabla.heading("FIRMA", text="FIRMA")
tabla.heading("HASH PREVIO", text="HASH PREVIO")
tabla.heading("VOTADO", text="VOTADO")
tabla.heading("TIMESTAMP", text="TIMESTAMP")
tabla.heading("CLAVE ELECTOR", text="CLAVE ELECTOR")
tabla.heading("ENTIDAD", text="ENTIDAD")
tabla.heading("ESTADO", text="ESTADO")
tabla.heading("SECCIÓN", text="SECCIÓN")

mostrarDatos(tabla)  # Limit the number of documents to 5





class Votar(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="black")
        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="Elegir Candidato", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        radio_var = tk.StringVar()


        opciones = {
            "Claudia Sheinbaum": "id1",
            "Xochitl Gálvez": "id2",
            "Adán Augusto López": "id3",
            "Samuel García": "id4"
        }


        for opcion, identificador in opciones.items():
            radio_button = tk.Radiobutton(
                self, foreground="White", bg="black", text=opcion, variable=radio_var, value=identificador)
            radio_button.pack(side="top", padx=25, pady=25)


        def check_inputs():
            selected_option = radio_var.get()
            if selected_option == "":
                return False
            else:
                print("Voto registrado al ID del candidato:", selected_option)
                return True


        button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2, padx=3, pady=3,
                           font="Verdana", text="Enviar voto", command=lambda: controller.show_frame("Gracias") if check_inputs() else None)
        button.pack()




class Gracias(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="¡Tu voto se registró con éxito!", font=controller.title_font)
        label.pack(side="top", fill="x")


        label = tk.Label(self, foreground="Purple", bg="black", height=30, width=350,
                         text="¡Gracias por votar!\n\nVoto contabilizado y vinculado al\n Presupuesto Participativo de tu comunidad\n\nIMPRESIÓN de BOLETA en alcaldía en tiempo real\n(voto encriptado: timestamp y candidato electo)\neyJhbGciIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6I")
        label.pack()
        button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white",
                           bd=2, padx=3, pady=3, font="Verdana", text="Cerrar", command=lambda: self.controller.destroy())
        button.pack()




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()



