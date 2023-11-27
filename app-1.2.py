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
from PIL import Image, ImageTk


uri = "mongodb+srv://mongo:Miuniversidad2023@cluster0.sfa5efq.mongodb.net/?retryWrites=true&w=majority"
cliente_mongo = MongoClient(uri, server_api=ServerApi('1'))
barcode_data = str()  # Variable global
cliente = cliente_mongo
baseDatos = cliente["padron"]
coleccion = baseDatos["padron1"]            
# Realiza la búsqueda en la colección usando los datos del código QR
query = {"clave_elector": {"$regex":".*" + barcode_data + ".*"}}
result = coleccion.find_one(query)


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Verdana', size=16)
        self.cuerpo_font = tkfont.Font(family='Verdana', size=12)
        self.geometry("500x950")
        self.title("ParticipoMX")
        self.resizable(0,0)
        self.iconbitmap("logo.ico")
        self.configure(bg="black")
        self.cliente_mongo = pymongo.MongoClient(uri, serverSelectionTimeOutMS=5000)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (Portada, Inicio, ConfirmarDatos, Votar, Gracias):
            page_name = F.__name__
            frame = F(parent=container, controller=self, cliente_mongo=self.cliente_mongo)
            frame.configure(bg="black")
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("Portada")

    def show_frame(self, page_name,barcode_data=None,result=None):
        frame = self.frames[page_name]
        frame.controller=self
        frame.cliente_mongo=self.cliente_mongo
        frame.barcode_data=barcode_data
        frame.result=result
        frame.tkraise()
        

                
class Portada(tk.Frame):
    def __init__(self, parent, controller, cliente_mongo, barcode_data=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cliente_mongo = cliente_mongo
        # Resto del código de inicialización de la clase

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
                            padx=3, pady=3, font="Verdana", text="Comienza escaneando el QR de tu INE", command=lambda: controller.show_frame("Inicio"))
        button1.pack()


class Inicio(tk.Frame):
    def __init__(self, parent, controller, cliente_mongo):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cliente_mongo = cliente_mongo

        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="1. Escanea el código QR \nbidimensional de tu INE", font=controller.title_font)
        label.pack(side="top", fill="x")

        self.video_label = tk.Label(self)
        self.video_label.pack()

        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 350)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
        self.capture_qr()

    def capture_qr(self):
        global barcode_data  # Indicar que se utilizará la variable global
        success, frame = self.cam.read()

        if success:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcodes = pyzbar.decode(gray_frame)
            self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            barcode_data=barcode_data

            ##for (x, y, w, h) in faces:
                ##cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                ##face_gray = gray_frame[y:y+h,x:x+w]
                ##barcodes = pyzbar.decode(face_gray)

            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type
                print("Barcode Type:", barcode_type)
                print("Barcode Data:", barcode_data)             
                barcode_data == barcode_data

                query = {"clave_elector": {"$regex":".*" + barcode_data + ".*"}}
                result = coleccion.find_one(query)
                
                if result:
                    ##self.controller.show_frame("ConfirmarDatos", barcode_data, result)
                    button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2, padx=3, pady=3,
                                    font="Verdana", text="Continuar", command=lambda: self.show_frame("Votar") if check_inputs(input_vars) else None)
                    button.pack()
                else:
                    # No se encontró ningún documento que coincida con los datos del código QR
                    print("No se encontró ningún documento para los datos del código QR")


        self.display_video(frame)
        self.video_label.after(10, self.capture_qr)

    def display_video(self, frame):
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image.thumbnail((350, 450))
        photo = ImageTk.PhotoImage(image)
        self.video_label.configure(image=photo)
        self.video_label.image = photo




class ConfirmarDatos(tk.Frame):
    def __init__(self, parent, controller, cliente_mongo):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cliente_mongo = cliente_mongo

        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="Confirma tus datos", font=controller.title_font)
        label.pack(side="top", fill="x")
        if result==True:
            datos = [
                ("NOMBRE", datos["nombre"]),
                ("APELLIDO PATERNO", datos["apellido_paterno"]),
                ("APELLIDO MATERNO", datos["apellido_materno"]),
                ("FIRMA", datos["firma"]),
                ("CLAVE ELECTOR", datos["clave_elector"]),
                ("ENTIDAD", datos["entidad"]),
                ("ESTADO", datos["estado"]),
                ("SECCIÓN", datos["seccion"])
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
                            font="Verdana", text="Continuar", command=lambda: self.controller.show_frame("Votar") if check_inputs(input_vars) else None)
            button.pack()

def check_inputs(input_vars):
    # Verificar si todos los campos de entrada tienen valores no vacíos
    for var in input_vars:
        if var.get() == "":
            return False
    return True



class Votar(tk.Frame):
    def __init__(self, parent, controller, cliente_mongo):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cliente_mongo = cliente_mongo
        # Resto del código de inicialización de la clase    
        image_path = "ine-card.jpg"  # Updated image file path
        image = ImageTk.PhotoImage(file=image_path)  # Ruta de la imagen que deseas mostrar

        label = tk.Label(self, image=image, bg="black")
        label.image = image  # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        label.pack(side="top")


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
                foreground="Gray",
                bg="black",
                text=opcion,
                variable=radio_var,
                value=identificador,
                indicatoron=0,
                height=2,
                width=150,
                relief="groove",
                bd=2,
                padx=3,
                pady=3,
                font="Verdana",
            )
            radio_button.pack(side="top")

        button = tk.Button(
            self,
            height=3,
            width=120,
            bg="purple",
            relief="groove",
            foreground="white",
            bd=2,
            padx=3,
            pady=3,
            font="Verdana",
            text="Confirmar voto",
            command=lambda: self.registrar_voto(radio_var.get(), controller)
        )
        button.pack()

    def registrar_voto(self, candidato_id, controller):
        if candidato_id != "":
            try:
                cliente = self.cliente_mongo
                baseDatos = cliente["padron"]
                coleccion = baseDatos["padron1"]

                coleccion.find_one_and_replace({"clave_elector": {"$regex": ".*\d.*12.*"}},{"votado": candidato_id})

                cliente.server_info()
                print("Voto registrado al ID del candidato:", candidato_id)
                print("Actualización exitosa")

                controller.show_frame("Gracias")  # Redirigir al frame "Gracias"

            except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
                print("Tiempo excedido " + str(errorTiempo))
            except pymongo.errors.ConnectionFailure as errorConexion:
                print("Fallo al conectarse a MongoDB " + str(errorConexion))
        else:
            print("No se seleccionó ningún candidato")

                


class Gracias(tk.Frame):
    def __init__(self, parent, controller, cliente_mongo):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cliente_mongo = cliente_mongo
        # Resto del código de inicialización de la clase

        image_path = "ine-vote.jpg"  # Updated image file path
        image = ImageTk.PhotoImage(file=image_path)  # Ruta de la imagen que deseas mostrar

        label = tk.Label(self, image=image, bg="black")
        label.image = image  # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        label.pack(side="top")



        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="¡Tu voto se registró con éxito!", font=controller.title_font)
        label.pack(side="top", fill="x")


        label = tk.Label(self, foreground="White", bg="black", height=13, width=350,
                         text="¡Gracias por votar!\n\nVoto contabilizado y vinculado al\n Presupuesto Participativo de tu comunidad\n\nIMPRESIÓN de BOLETA en alcaldía en tiempo real\n(voto encriptado: timestamp y candidato electo)\n\neyJhbGciIs", font=controller.cuerpo_font)
        label.pack()


        button = tk.Button(self, height=3, width=150, bg="white", relief="flat", foreground="purple",
                           bd=2, padx=3, pady=3, font="Verdana", text="Descargar boleta", command=lambda: self.controller.destroy())
        button.pack()


        button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white",
                           bd=2, padx=3, pady=3, font="Verdana", text="Cerrar", command=lambda: self.controller.destroy())
        button.pack()

def __del__(self):
    self.cliente_mongo.close()
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
