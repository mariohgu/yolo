import os
import glob

# Ubicación actual del script
ubicacion = os.path.dirname(os.path.abspath(__file__))

# Directorio de entrada
input_dir = os.path.join(ubicacion, "input")

# Obtiene todos los archivos .jpg en el directorio
files = glob.glob(os.path.join(input_dir, "*.jpg"))

for fil in files:
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]
    xml_file = os.path.join(input_dir, f"{filename}.xml")

    # Verifica si el archivo XML correspondiente no existe
    if not os.path.exists(xml_file):
        os.remove(
            fil
        )  # Borra el archivo .jpg si no hay un archivo .xml correspondiente

print("Fin")
