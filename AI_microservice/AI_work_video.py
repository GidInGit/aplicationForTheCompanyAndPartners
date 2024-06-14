from ultralytics import YOLO
import cv2

# Загрузка предварительно обученной модели YOLOv8
model = YOLO('/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/runs/detect/train2/weights/last.pt')  # Используем YOLOv8n (nano) модель, можно также выбрать другие версии, например yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt

# Открываем видеофайл
video_path = 'video/Заливка фундамента в Московской области __ Благоустройство.рф.mp4'
cap = cv2.VideoCapture(video_path)

# Получаем свойства видео
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Настраиваем видеозапись
output_path = 'output_video'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Обработка видео
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Выполнение предсказания
    results = model(frame)

    # Визуализация результатов
    for result in results:
        boxes = result.boxes.xyxy  # Получаем координаты ограничивающих рамок
        confidences = result.boxes.conf  # Получаем уверенность предсказаний
        class_ids = result.boxes.cls  # Получаем метки классов

        # Рисуем ограничивающие рамки на изображении (если используем OpenCV)
        for box, conf, cls_id in zip(boxes, confidences, class_ids):
            # if int(cls_id) == 0:  # Фильтруем по классу "человек"
                x1, y1, x2, y2 = map(int, box)  # Преобразуем координаты в int
                label = model.names[int(cls_id)]  # Получаем имя класса
                score = float(conf)  # Получаем уверенность предсказания

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {score:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Записываем обработанный кадр
    out.write(frame)

    # Отображаем кадр (если нужно)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
out.release()
cv2.destroyAllWindows()
