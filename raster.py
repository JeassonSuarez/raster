from PIL import Image

def convert_to_tiff(input_image_path, output_tiff_path):
    try:
        # Abrir la imagen de entrada
        image = Image.open(input_image_path)

        # Guardar la imagen en formato TIFF
        image.save(output_tiff_path, "TIFF")

        print(f"Imagen convertida exitosamente a {output_tiff_path}")

    except Exception as e:
        print(f"Error al convertir la imagen: {e}")

if __name__ == "__main__":
    input_image_path = "./bogota.jpg"  # Ruta de la imagen de entrada (cambia esto)
    output_tiff_path = "./imagen.tiff"  # Ruta de la imagen de salida (cambia esto)

    convert_to_tiff(input_image_path, output_tiff_path)