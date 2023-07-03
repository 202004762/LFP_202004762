from tkinter import Tk
from tkinter.filedialog import askopenfilename


class Lector:

    @staticmethod
    def file_reader(type_file):
        data = ""
        text = ""

        Tk().withdraw()
        file = askopenfilename(
            title = "Selecciona un archivo .data",
            initialdir = "./",
            filetypes = (
                ("Archivo", f"*{type_file}"),
                ("Todos los archivos", "*.*")
            )
        )
        
        if file == "":
            print("- Ningun archivo seleccionado \n")
            return None
        else:
            with open(file, encoding='utf-8') as infile:
                text = infile.read().strip()
        
        if file is None:
            print("- Ningun archivo seleccionado \n")
            return None
        else:            
            flag = False
            for letter in text:
                if letter != '\"':
                    if (letter != " " and letter !="\t") or flag:
                        data += letter

                elif not flag:
                    data += letter
                    flag = True

                else:
                    data += letter
                    flag = False

            print("- Lectura exitosa \n")
            return data