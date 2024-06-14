from PIL import Image
import os

# Путь к папке с изображениями WebP
input_folder = './downloaded_images'
# Путь к папке для сохранения изображений PNG
output_folder = './converted_files'
os.makedirs(output_folder, exist_ok=True)

# Проход по всем файлам в папке с изображениями WebP
for filename in os.listdir(input_folder):
    if filename.endswith('.webp'):
        webp_path = os.path.join(input_folder, filename)
        png_path = os.path.join(output_folder, filename.replace('.webp', '.png'))

        # Открытие изображения и конвертация
        with Image.open(webp_path) as img:
            img.save(png_path, 'PNG')
            print(f"Сконвертировано: {filename} -> {os.path.basename(png_path)}")

print("Все изображения сконвертированы.")
