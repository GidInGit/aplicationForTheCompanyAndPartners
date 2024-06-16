from ultralytics import YOLO
import cv2
# import matplotlib.pyplot as plt

# Загрузка предварительно обученной модели YOLOv8
model = YOLO(r"C:\Users\reben\PycharmProjects\aplicationForTheCompanyAndPartners\runs\detect\yolov8n_v8_50e2\weights\last.pt")

# Загрузка и обработка изображения
image_path = r'photo\1557360052_0_158_3077_1889_600x0_80_0_0_69193f341735da27d1b7388575cc8682.jpg'
image = cv2.imread(image_path)

# Выполнение предсказания
results = model(image)

# Отображение результатов
# Визуализация результатов
for result in results:
    boxes = result.boxes.xyxy  # Получаем координаты ограничивающих рамок
    confidences = result.boxes.conf  # Получаем уверенность предсказаний
    class_ids = result.boxes.cls  # Получаем метки классов

    # Рисуем ограничивающие рамки на изображении (если используем OpenCV)
    for box, conf, cls_id in zip(boxes, confidences, class_ids):
        x1, y1, x2, y2 = map(int, box)  # Преобразуем координаты в int
        label = model.names[int(cls_id)]  # Получаем имя класса
        score = float(conf)  # Получаем уверенность предсказания

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"{label} {score:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Отображаем изображение с предсказаниями с помощью OpenCV
cv2.imshow('Predictions', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


