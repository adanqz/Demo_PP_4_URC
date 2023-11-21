import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import ttk
from tkinter import messagebox


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

        frame = tk.Frame(self, bg="gray", width=250, height=600)
        frame.pack(side="top", fill="x")

        button1 = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white", bd=2,
                            padx=3, pady=3, font="Verdana", text=">>>", command=lambda: controller.show_frame("ReconocimientoFacial"))
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
        etiquetas = ["CIC", "ID Ciudadano OCR", "Nombre", "Apellido Paterno", "Apellido Materno", "Entidad", "Municipio",
                     "Sección", "Vigencia", "Fotografía con marca de agua", "CPV Nacional Extranjera", "Imagen de Huella", "Firma Digital"]
        valores_predeterminados = ["1836554780", "7485914758624", "", "", "", "0140", "CDMX", "045", "2027",
                                   "0101010101010010101011010101010101", "1452", "01111010111101011001110100101010110010", "fx01219223923892943983948xcs92389283"]

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

        label = tk.Label(self, foreground="Purple", bg="black", height=40, width=350,
                         text="¡Gracias por votar!\n\nVoto contabilizado y vinculado al\n Presupuesto Participativo de tu comunidad\n\nIMPRESIÓN de BOLETA en alcaldía en tiempo real\n(voto encriptado: timestamp y candidato electo)\neyJhbGciIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6I")
        label.pack()
        button = tk.Button(self, height=3, width=150, bg="purple", relief="groove", foreground="white",
                           bd=2, padx=3, pady=3, font="Verdana", text="Cerrar", command=lambda: self.controller.destroy())
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
