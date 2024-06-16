from ultralytics import YOLO
def main():
    # Создание объекта модели YOLO и загрузка предобученной модели
    model = YOLO(r'yolov8m.pt')  # Используем YOLOv8n (nano) модель

    # Путь к файлу конфигурации набора данных
    data_path = 'data_set_new/data.yaml'

    # Обучение модели
    model.train(data=data_path,
                imgsz=640,
                epochs=50,
                batch=8,
                workers=8,  # Устанавливаем количество рабочих процессов для загрузки данных
                name='yolov8n_v8_50e'
                )

    # Сохранение обученной модели
    model.save()

if __name__ == '__main__':
    main()