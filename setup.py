from setuptools import setup
import os

# Definimos los archivos extra (como la imagen de la nube)
DATA_FILES = []
if os.path.exists("nube.png"):
    DATA_FILES.append("nube.png")

APP = ['neoos.pyw']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['customtkinter', 'PIL'], # Forzamos la inclusión de las librerías
    'plist': {
        'CFBundleName': 'NeoOS',
        'CFBundleDisplayName': 'NeoOS Alpha',
        'CFBundleIdentifier': 'com.neoos.alpha',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
