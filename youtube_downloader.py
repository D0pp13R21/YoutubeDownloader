import tkinter as tk
from tkinter import ttk
import pytube

def download_video():
    url = link_entry.get()
    resolution = resolution_combobox.get()
    try:
        video = pytube.YouTube(url)
        if video.age_restricted:
            status_label.config(text="Este vídeo possui restrição de idade. Não é possível fazer o download.")
        else:
            stream = video.streams.get_by_resolution(resolution)
            if stream:
                stream.download()
                status_label.config(text="Download concluído!")
            else:
                status_label.config(text="Resolução não suportada!")
    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}")

# Criação da janela principal
window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("400x150")

# Criação e posicionamento dos widgets
link_label = ttk.Label(window, text="Insira o link do vídeo:")
link_label.pack()

link_entry = ttk.Entry(window, width=50)
link_entry.pack()

resolution_label = ttk.Label(window, text="Selecione a resolução:")
resolution_label.pack()

resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
resolution_combobox = ttk.Combobox(window, values=resolutions)
resolution_combobox.pack()

download_button = ttk.Button(window, text="Baixar", command=download_video)
download_button.pack()

status_label = ttk.Label(window, text="")
status_label.pack()

# Loop principal da janela
window.mainloop()
