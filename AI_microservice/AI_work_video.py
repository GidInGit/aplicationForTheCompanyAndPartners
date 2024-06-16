from ultralytics import YOLO
import cv2
import time

# Загрузка предварительно обученной модели YOLOv8
model = YOLO(
    r"C:\Users\reben\PycharmProjects\aplicationForTheCompanyAndPartners\runs\detect\yolov8n_v8_50e2\weights\last.pt")

# Открываем видеофайл
video_path = r'video\Заливка фундамента в Московской области __ Благоустройство.рф.mp4'
cap = cv2.VideoCapture(video_path)

# Получаем свойства видео
fps = 60  # Ограничиваем частоту кадров до 60
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Настраиваем видеозапись
output_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Обработка видео
while cap.isOpened():
    start_time = time.time()

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

    # Ограничиваем частоту кадров до 60
    elapsed_time = time.time() - start_time
    time_to_wait = max(0, (1.0 / fps) - elapsed_time)
    time.sleep(time_to_wait)

# Освобождаем ресурсы
cap.release()
out.release()
cv2.destroyAllWindows()
