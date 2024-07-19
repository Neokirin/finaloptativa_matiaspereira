import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import json

def iniciar_juego():
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'mati.py')
    if os.path.exists(ruta_archivo):
        subprocess.run(["python", ruta_archivo])
    else:
        messagebox.showerror("Error", "El archivo 'mati.py' no se encuentra en la carpeta actual.")

def ver_puntuaciones():
    if os.path.exists('scores.json'):
        with open('scores.json', 'r') as file:
            scores = json.load(file)
        
        if scores:
            scores_text = '\n'.join([f"{entry['name']}: {entry['score']}" for entry in scores])
        else:
            scores_text = "No hay puntuaciones guardadas."
    else:
        scores_text = "No hay archivo de puntuaciones encontrado."
    
    # Mostrar puntuaciones en un cuadro de diálogo
    messagebox.showinfo("Puntuaciones", scores_text)

def salir():
    root.destroy()

root = tk.Tk()
root.title("Menú Principal")
root.geometry("600x400")
root.configure(bg='black')

def crear_boton(texto, comando):
    boton = tk.Button(root, text=texto, command=comando, font=("Arial", 16), bg='black', fg='white', relief='flat', height=2, width=20)
    boton.pack(pady=20)
    return boton

crear_boton("Iniciar Juego", iniciar_juego)
crear_boton("Ver Puntuaciones", ver_puntuaciones)
crear_boton("Salir", salir)

root.mainloop()
