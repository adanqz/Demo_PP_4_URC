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
from pyzbar import pyzbar
import time
from PIL import ImageTk


uri = "mongodb+srv://mongo:Miuniversidad2023@cluster0.sfa5efq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Verdana', size=16)
        self.cuerpo_font = tkfont.Font(family='Verdana', size=12)
        self.geometry("500x950")
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
        for F in (Portada, Inicio, ConfirmarDatos, Votar, Gracias, ReconocimientoFacial):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.configure(bg="black")
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("Portada")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()





class Portada(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image_path = "ine-bd.jpg"  # Updated image file path
        image = ImageTk.PhotoImage(file=image_path)  # Ruta de la imagen que deseas mostrar

        label = tk.Label(self, image=image, bg="black")
        label.image = image  # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        label.pack(side="top")


        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="¡Participas tú! \n¡Ganamos todos!", font=controller.title_font)
        label.pack(side="top", fill="x")


        label = tk.Label(self, foreground="White", bg="black", height=12, text="Ahora tu voto influye en\nel Presupuesto Participativo de tu\ncomunidad. \n\nEl mejoramiento de nuestra \nsociedad \nestá al alcance de todos.\n\nUn voto con sentido,\nun voto con intención", font=controller.cuerpo_font)
        label.pack(side="top", fill="x")


        button1 = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2,
                            padx=3, pady=3, font="Verdana", text="Comienza escaneando tu INE", command=lambda: controller.show_frame("Inicio"))
        button1.pack()




class Inicio(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="1. Escanea el código QR \nbidimensional de tu INE", font=controller.title_font)
        label.pack(side="top", fill="x")


        cam = cv2.VideoCapture(0)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            success, frame = cam.read()

            barcodes = pyzbar.decode(frame)

            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type

                print("Barcode Type:", barcode_type)
                print("Barcode Data:", barcode_data)

                # Add your desired handling or processing of the barcode data here

            cv2.imshow("QR_Scanner", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()

        frame = tk.Frame(self, bg="gray", width=250, height=600)
        frame.pack(side="top", fill="x")

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

        try:
            cliente = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
            baseDatos = cliente["padron"]
            coleccion = baseDatos["padron1"]
            
            documento = coleccion.find_one({"clave_elector": {"$regex": ".*\d.*73.*"}})

            if documento:
                datos = [
                    ("ID", documento["_id"]),
                    ("NOMBRE", documento["nombre"]),
                    ("APELLIDO PATERNO", documento["apellido_paterno"]),
                    ("APELLIDO MATERNO", documento["apellido_materno"]),
                    ("ID", documento["id"]),
                    ("TELÉFONO", documento["telefono"]),
                    ("HASH ACTUAL", documento["hash_actual"]),
                    ("HASH PÚBLICO", documento["hash_publico"]),
                    ("FIRMA", documento["firma"]),
                    ("HASH PREVIO", documento["hash_previo"]),
                    ("VOTADO", documento["votado"]),
                    ("TIMESTAMP", documento["timestamp"]),
                    ("CLAVE ELECTOR", documento["clave_elector"]),
                    ("ENTIDAD", documento["entidad"]),
                    ("ESTADO", documento["estado"]),
                    ("SECCIÓN", documento["seccion"])
                ]

                input_vars = []

                for dato in datos:
                    label = tk.Label(self, foreground="White", bg="black", text=dato[0])
                    label.pack()

                    input_var = tk.StringVar()
                    input_var.set(dato[1])

                    entry = tk.Entry(self, textvariable=input_var)
                    entry.pack()
                    input_vars.append(input_var)

                button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2, padx=3, pady=3,
                                   font="Verdana", text="Continuar", command=lambda: controller.show_frame("Votar") if check_inputs(input_vars) else None)
                button.pack()
            else:
                print("No se encontraron documentos en la colección")

            cliente.server_info()
            print("Conexión a MongoDB exitosa")
            cliente.close()
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo excedido " + str(errorTiempo))
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a MongoDB " + str(errorConexion))

def check_inputs(input_vars):
    # Verificar si todos los campos de entrada tienen valores no vacíos
    for var in input_vars:
        if var.get() == "":
            return False
    return True




class Votar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="black")
        label = tk.Label(self, foreground="Purple", bg="black", height=3, text="Elegir Candidato", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        radio_var = tk.StringVar()

        opciones = {
            "Claudia Sheinbaum": "1",
            "Xochitl Gálvez": "2",
            "Adán Augusto López": "3",
            "Samuel García": "4"
        }

        for opcion, identificador in opciones.items():
            radio_button = tk.Radiobutton(
                self,
                foreground="White",
                bg="black",
                text=opcion,
                variable=radio_var,
                value=identificador
            )
            radio_button.pack(side="top", padx=25, pady=25)

        button = tk.Button(
            self,
            height=3,
            width=150,
            bg="purple",
            relief="groove",
            foreground="white",
            bd=2,
            padx=3,
            pady=3,
            font="Verdana",
            text="Continuar",
            command=lambda: self.registrar_voto(radio_var.get(), controller)
        )
        button.pack()

    def registrar_voto(self, candidato_id, controller):
        if candidato_id != "":
            try:
                cliente = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
                baseDatos = cliente["padron"]
                coleccion = baseDatos["padron1"]

                coleccion.find_one_and_replace({"clave_elector": {"$regex": ".*\d.*73.*"}},{"votado": candidato_id})

                cliente.server_info()
                print("Voto registrado al ID del candidato:", candidato_id)
                print("Actualización exitosa")
                cliente.close()

                controller.show_frame("Gracias")  # Redirigir al frame "Gracias"

            except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
                print("Tiempo excedido " + str(errorTiempo))
            except pymongo.errors.ConnectionFailure as errorConexion:
                print("Fallo al conectarse a MongoDB " + str(errorConexion))
        else:
            print("No se seleccionó ningún candidato")

                


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



