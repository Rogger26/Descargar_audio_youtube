# import tkinter as tk
# from tkinter import messagebox
# from pytube import YouTube
# import os

# def get_download_folder():
#     if os.name == 'nt':  # Windows
#         return os.path.join(os.environ['USERPROFILE'], 'Downloads')
#     else:  # MacOS/Linux
#         return os.path.join(os.path.expanduser('~'), 'Downloads')

# def download_audio():
#     url = url_entry.get()
#     if not url:
#         messagebox.showwarning("Entrada inválida", "Por favor, ingresa una URL de YouTube.")
#         return

#     try:
#         video = YouTube(url)
#         audio_stream = video.streams.get_audio_only()
#         save_path = get_download_folder()
#         audio_stream.download(output_path=save_path)
#         messagebox.showinfo("Descarga completada", f"El audio ha sido descargado en {save_path}")
#     except Exception as e:
#         messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

# # Configuración de la ventana principal
# root = tk.Tk()
# root.title("Descargador de Audio de YouTube")

# # Creación de los elementos de la GUI
# url_label = tk.Label(root, text="URL del video de YouTube:")
# url_label.pack(pady=5)

# url_entry = tk.Entry(root, width=50)
# url_entry.pack(pady=5)

# download_button = tk.Button(root, text="Descargar Audio", command=download_audio)
# download_button.pack(pady=20)

# # Iniciar el bucle principal de la GUI
# root.mainloop()

from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
import os

app = Flask(__name__)

def get_download_folder():
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # MacOS/Linux
        return os.path.join(os.path.expanduser('~'), 'Downloads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    if not url:
        return redirect(url_for('index'))

    try:
        video = YouTube(url)
        audio_stream = video.streams.get_audio_only()
        save_path = get_download_folder()
        file_path = audio_stream.download(output_path=save_path)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Ha ocurrido un error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
