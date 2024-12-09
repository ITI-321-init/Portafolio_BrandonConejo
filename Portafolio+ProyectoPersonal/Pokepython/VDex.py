from math import trunc

import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from io import BytesIO
import random

# Función para realizar la solicitud a la API de Pokémon
def pokedex(name, url_base="https://pokeapi.co/api/v2/"):
    url = f"{url_base}pokemon/{name.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        messagebox.showerror("Error", f"Pokémon no encontrado. Código de error: {respuesta.status_code}")
        return None

# Función para mostrar la información del Pokémon en la interfaz
def mostrar_info(nombre=None):
    if not nombre:
        nombre = entrada_nombre.get().strip().lower()
    if not nombre:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre de un Pokémon.")
        return

    datos_pokemon = pokedex(nombre)
    if datos_pokemon:
        # Determinar si es shiny
        shiny = random.randint(1, 1) == 1  # Probabilidad de 1 en 20
        sprite_key = 'front_shiny' if shiny else 'front_default'
        texto_color = "blue" if shiny else "black"

        # Limpiar contenido previo
        for widget in frame_info.winfo_children():
            widget.destroy()

        # Mostrar la información relevante del Pokémon
        tk.Label(
            frame_info,
            text=f"Nombre: {datos_pokemon['name'].capitalize()} {'(Shiny)' if shiny else ''}",
            font=("Arial", 14, "bold"),
            fg=texto_color
        ).pack(anchor="w", pady=5)
        tk.Label(frame_info, text=f"ID: {datos_pokemon['id']}", font=("Arial", 12)).pack(anchor="w")
        tipos = ", ".join([tipo['type']['name'].capitalize() for tipo in datos_pokemon['types']])
        tk.Label(frame_info, text=f"Tipo(s): {tipos}", font=("Arial", 12)).pack(anchor="w")
        altura = datos_pokemon['height'] / 10  # Convertir a metros
        peso = datos_pokemon['weight'] / 10  # Convertir a kilogramos
        tk.Label(frame_info, text=f"Altura: {altura} m", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame_info, text=f"Peso: {peso} kg", font=("Arial", 12)).pack(anchor="w")

        # Descargar y mostrar la imagen del Pokémon (normal o shiny)
        try:
            url_imagen = datos_pokemon['sprites']['other']['official-artwork'][sprite_key]
            if not url_imagen:  # Si no hay shiny en 'official-artwork', usar sprite normal
                url_imagen = datos_pokemon['sprites']['front_shiny' if shiny else 'front_default']
            respuesta_imagen = requests.get(url_imagen)
            imagen = Image.open(BytesIO(respuesta_imagen.content))
            imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)

            label_imagen = tk.Label(frame_info, image=imagen_tk, bg="white")
            label_imagen.image = imagen_tk
            label_imagen.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen del Pokémon. Detalles: {e}")

# Función para buscar un Pokémon al azar
def buscar_azar():
    max_pokemon_id = 1010  # Número máximo de Pokémon disponibles en la API
    id_aleatorio = random.randint(1, max_pokemon_id)
    mostrar_info(str(id_aleatorio))

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Pokedex Visual")
ventana.geometry("400x550")
ventana.resizable(True, True)

# Frame para la entrada del nombre
frame_input = tk.Frame(ventana)
frame_input.pack(pady=10)
tk.Label(frame_input, text="Ingrese el nombre del Pokémon:", font=("Arial", 12)).pack(side="left", padx=5)
entrada_nombre = ttk.Entry(frame_input, width=20)
entrada_nombre.pack(side="left", padx=5)
boton_buscar = ttk.Button(frame_input, text="Buscar", command=mostrar_info)
boton_buscar.pack(side="left", padx=5)

# Botón para buscar un Pokémon al azar
boton_azar = ttk.Button(ventana, text="Buscar al Azar", command=buscar_azar)
boton_azar.pack(pady=10)

# Frame para mostrar la información
frame_info = tk.Frame(ventana, bg="white", relief="groove", borderwidth=2)
frame_info.pack(pady=10, fill="both", expand=True)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
