import os
import shutil
from sklearn.model_selection import train_test_split

# Путь к исходным данным и аннотациям
source_images_path = '/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/AI_microservice/yolo_data/images'
source_labels_path = '/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/AI_microservice/yolo_data/labels'
output_path = 'data_set'

# Создание структуры папок
os.makedirs(os.path.join(output_path, 'images/train'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'images/val'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'labels/train'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'labels/val'), exist_ok=True)

# Список всех изображений и аннотаций
images = sorted([f for f in os.listdir(source_images_path) if f.endswith('.png')])
annotations = sorted([f for f in os.listdir(source_labels_path) if f.endswith('.txt')])

# Проверка на совпадение количества изображений и аннотаций
assert len(images) == len(annotations), "Количество изображений и аннотаций должно быть одинаковым"

# Разделение данных на тренировочный и валидационный наборы
train_images, val_images, train_annotations, val_annotations = train_test_split(
    images, annotations, test_size=0.2, random_state=42
)

# Функция для копирования файлов
def copy_files(file_list, source_folder, destination_folder):
    for file in file_list:
        shutil.copy(os.path.join(source_folder, file), os.path.join(destination_folder, file))

# Копирование файлов в соответствующие папки
copy_files(train_images, source_images_path, os.path.join(output_path, 'images/train'))
copy_files(val_images, source_images_path, os.path.join(output_path, 'images/val'))
copy_files(train_annotations, source_labels_path, os.path.join(output_path, 'labels/train'))
copy_files(val_annotations, source_labels_path, os.path.join(output_path, 'labels/val'))

# Создание конфигурационного файла data.yaml
data_yaml_content = f"""
train: {os.path.join(output_path, 'images/train')}
val: {os.path.join(output_path, 'images/val')}
nc: 1  # Number of classes
names: ['helmet']  # Class names
"""

with open(os.path.join(output_path, 'data.yaml'), 'w') as f:
    f.write(data_yaml_content)

print("Данные успешно организованы и готовы к использованию с YOLOv8.")
