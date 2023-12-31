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
client = MongoClient(uri, server_api=ServerApi('1'))


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Verdana', size=16)
        self.cuerpo_font = tkfont.Font(family='Verdana', size=12)
        self.geometry("500x950")
        self.title("ParticipoMX")
        self.configure(bg="black")
        self.resizable(0,0)
        self.iconbitmap("logo.ico")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (Portada, Inicio, ReconocimientoFacial, ConfirmarDatos, Votar, Gracias):
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

        image_path = "ine-ub.jpg"  # Updated image file path
        image = ImageTk.PhotoImage(file=image_path)  # Ruta de la imagen que deseas mostrar

        label = tk.Label(self, image=image, bg="black")
        label.image = image  # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        label.pack(side="top")


        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="1. Escanea el código QR \nbidimensional de tu INE", font=controller.title_font)
        label.pack(side="top", fill="x")

        self.video_label = tk.Label(self)
        self.video_label.pack()

        button1 = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2,
                            padx=3, pady=3, font="Verdana", text="O acceder al >> Reconocimiento facial", command=lambda: controller.show_frame("ReconocimientoFacial"))
        button1.pack()

        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 350)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

        self.capture_qr()



    def capture_qr(self):
        success, frame = self.cam.read()

        if success:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
        # Detect faces using the cascade classifier
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                face_gray = gray_frame[y:y+h,x:x+w]
                barcodes = pyzbar.decode(face_gray)

                for barcode in barcodes:
                    barcode_data = barcode.data.decode('utf-8')
                    barcode_type = barcode.type

                    print("Barcode Type:", barcode_type)
                    print("Barcode Data:", barcode_data)

        self.display_video(frame)
        self.video_label.after(10, self.capture_qr)

    def display_video(self, frame):
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image.thumbnail((350, 450))
        photo = ImageTk.PhotoImage(image)
        self.video_label.configure(image=photo)
        self.video_label.image = photo



class ReconocimientoFacial(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image_path = "ine-institute.jpg"  # Updated image file path
        image = ImageTk.PhotoImage(file=image_path)  # Ruta de la imagen que deseas mostrar

        label = tk.Label(self, image=image, bg="black")
        label.image = image  # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        label.pack(side="top")


        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="Reconocimiento Facial", font=controller.title_font)
        label.pack(side="top", fill="x")


        frame = tk.Frame(self, bg="green", width=250, height=300)
        frame.pack(side="top", fill="x")


        button1 = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2,
                            padx=3, pady=3, font="Verdana", text="Confirmar Datos", command=lambda: controller.show_frame("ConfirmarDatos"))
        button1.pack()



class ConfirmarDatos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        try:
            cliente = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
            baseDatos = cliente["padron"]
            collection = baseDatos["padron1"]
            documento_initial = collection.find_one({"clave_elector": {"$regex": ".*\d.*73.*"}})

            if documento_initial:
                nombre = documento_initial["nombre"]
                apellido_paterno = documento_initial["apellido_paterno"]
                apellido_materno = documento_initial["apellido_materno"]
                telefono = documento_initial["telefono"]
                hash_actual = documento_initial["hash_actual"]
                hash_publico = documento_initial["hash_publico"]
                firma = documento_initial["firma"]
                clave_elector = documento_initial["clave_elector"]
                entidad = documento_initial["entidad"]
                estado = documento_initial["estado"]
                seccion = documento_initial["seccion"]

                # Clear the frame
                for widget in self.winfo_children():
                    widget.destroy()

                # Create labels for the desired fields
                label_nombre = tk.Label(self, foreground="White", bg="black", text="Nombre")
                label_nombre.pack()
                entry_nombre = tk.Entry(self)
                entry_nombre.insert(tk.END, nombre)
                entry_nombre.configure(state="readonly")
                entry_nombre.pack()

                label_apellido_paterno = tk.Label(self, foreground="White", bg="black", text="Apellido Paterno")
                label_apellido_paterno.pack()
                entry_apellido_paterno = tk.Entry(self)
                entry_apellido_paterno.insert(tk.END, apellido_paterno)
                entry_apellido_paterno.pack()

                label_apellido_materno = tk.Label(self, foreground="White", bg="black", text="Apellido Materno")
                label_apellido_materno.pack()
                entry_apellido_materno = tk.Entry(self)
                entry_apellido_materno.insert(tk.END, apellido_materno)
                entry_apellido_materno.pack()

                label_telefono = tk.Label(self, foreground="White", bg="black", text="Teléfono")
                label_telefono.pack()
                entry_telefono = tk.Entry(self)
                entry_telefono.insert(tk.END, telefono)
                entry_telefono.pack()


                label_hash_actual = tk.Label(self, foreground="White", bg="black", text="Hash Actual")
                label_hash_actual.pack()
                entry_hash_actual = tk.Entry(self)
                entry_hash_actual.insert(tk.END, hash_actual)
                entry_hash_actual.configure(state="readonly")
                entry_hash_actual.pack()

                label_hash_publico = tk.Label(self, foreground="White", bg="black", text="Hash Público")
                label_hash_publico.pack()
                entry_hash_publico = tk.Entry(self)
                entry_hash_publico.insert(tk.END, hash_publico)
                entry_hash_publico.configure(state="readonly")
                entry_hash_publico.pack()

                label_firma = tk.Label(self, foreground="White", bg="black", text="Firma")
                label_firma.pack()
                entry_firma = tk.Entry(self)
                entry_firma.insert(tk.END, firma)
                entry_firma.configure(state="readonly")
                entry_firma.pack()

                label_clave_elector = tk.Label(self, foreground="White", bg="black", text="Clave Elector")
                label_clave_elector.pack()
                entry_clave_elector = tk.Entry(self)
                entry_clave_elector.insert(tk.END, clave_elector)
                entry_clave_elector.configure(state="readonly")
                entry_clave_elector.pack()
    
                label_entidad = tk.Label(self, foreground="White", bg="black", text="Entidad")
                label_entidad.pack()
                entry_entidad = tk.Entry(self)
                entry_entidad.insert(tk.END, entidad)
                entry_entidad.configure(state="readonly")
                entry_entidad.pack()


                label_estado = tk.Label(self, foreground="White", bg="black", text="Estado")
                label_estado.pack()
                entry_estado = tk.Entry(self)
                entry_estado.insert(tk.END, estado)
                entry_estado.configure(state="readonly")
                entry_estado.pack()

                label_seccion = tk.Label(self, foreground="White", bg="black", text="Sección")
                label_seccion.pack()
                entry_seccion = tk.Entry(self)
                entry_seccion.insert(tk.END, seccion)
                entry_seccion.configure(state="readonly")
                entry_seccion.pack()

                button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2, padx=3, pady=3,
                                   font="Verdana", text="Continuar", command=lambda: self.ConfirmarDatos(entry_nombre.get(),entry_apellido_paterno.get(),entry_apellido_materno.get(),entry_telefono.get(),entry_hash_actual.get(),entry_hash_publico.get(),entry_firma.get(),entry_clave_elector.get(),entry_entidad.get(),entry_estado.get(),entry_seccion.get(), controller))
                button.pack()

            else:
                print("No document found for the given criteria.")

            cliente.server_info()
            print("Conexión a MongoDB exitosa")
            cliente.close()
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo excedido " + str(errorTiempo))
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a MongoDB " + str(errorConexion))



class Votar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
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


        image_path = "ine-vote.jpg"  # Updated image file path
        image = ImageTk.PhotoImage(file=image_path)  # Ruta de la imagen que deseas mostrar

        label = tk.Label(self, image=image, bg="black")
        label.image = image  # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        label.pack(side="top")



        label = tk.Label(self, foreground="Purple", bg="black", height=3,
                         text="¡Tu voto se registró con éxito!", font=controller.title_font)
        label.pack(side="top", fill="x")


        label = tk.Label(self, foreground="White", bg="black", height=13, width=350,
                         text="¡Gracias por votar!\n\nVoto contabilizado y vinculado al\n Presupuesto Participativo de tu comunidad\n\nIMPRESIÓN de BOLETA en alcaldía en tiempo real\n(voto encriptado: timestamp y candidato electo)\neyJhbGciIsInR5cCI6IkpXVCJ9\n.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6I", font=controller.cuerpo_font)
        label.pack()


        button = tk.Button(self, height=3, width=150, bg="white", relief="flat", foreground="purple",
                           bd=2, padx=3, pady=3, font="Verdana", text="Descargar boleta", command=lambda: self.controller.destroy())
        button.pack()


        button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white",
                           bd=2, padx=3, pady=3, font="Verdana", text="Cerrar", command=lambda: self.controller.destroy())
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
