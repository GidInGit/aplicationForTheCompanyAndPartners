from ultralytics import YOLO

# Создание объекта модели YOLO и загрузка предобученной модели
model = YOLO('yolov8n.pt')  # Используем YOLOv8n (nano) модель

# Путь к файлу конфигурации набора данных
data_path = 'data_set/data.yaml'

# Обучение модели
model.train(data=data_path, epochs=10, imgsz=640, workers=4)

# Сохранение обученной модели
model.save('/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/AI_microservice/AI')