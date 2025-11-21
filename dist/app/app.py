import webview
import subprocess
import time
import os

def start_server():
    # Ruta al manage.py dentro del EXE
    base_dir = os.path.abspath(os.path.dirname(__file__))
    manage_path = os.path.join(base_dir, "manage.py")

    # Inicia el servidor Django
    return subprocess.Popen(
        ['python', manage_path, 'runserver', '127.0.0.1:8000'],
        cwd=base_dir
    )

if __name__ == '__main__':
    p = start_server()
    time.sleep(3)  # Espera el servidor

    window = webview.create_window("ASSdelivery", "http://127.0.0.1:8000")
    webview.start()

    p.terminate()
