import os
import xml.etree.ElementTree as ET

# Путь к папке с изображениями и аннотациями
image_folder = '/path/to/images'
annotation_folder = '/path/to/xml_annotations'
output_folder = '/path/to/yolo_annotations'

# Создание папки для YOLO-аннотаций, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Список классов, которые нужно конвертировать в YOLO-формат
classes = ['helmet']  # Замените на ваши классы

# Функция для преобразования координат
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# Список всех XML-аннотаций
xml_files = [f for f in os.listdir(annotation_folder) if f.endswith('.xml')]

for xml_file in xml_files:
    xml_path = os.path.join(annotation_folder, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    annotation_file = os.path.splitext(xml_file)[0] + '.txt'
    annotation_path = os.path.join(output_folder, annotation_file)

    with open(annotation_path, 'w') as out_file:
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            if int(difficult) == 1:
                continue
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

print("Аннотации успешно преобразованы в формат YOLO.")
