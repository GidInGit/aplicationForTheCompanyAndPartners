# from ultralytics import YOLO
# import cv2
# import matplotlib.pyplot as plt
#
# # Загрузка предварительно обученной модели YOLOv8
# model = YOLO('/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/AI_microservice/runs/detect/train2/weights/last.pt')  # Используем YOLOv8n (nano) модель, можно также выбрать другие версии, например yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt
#
# # Загрузка и обработка изображения
# image_path = '/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/AI_microservice/runs/detect/train2/val_batch0_pred.jpg'
# image = cv2.imread(image_path)
#
# # Выполнение предсказания
# results = model(image)
#
# # Отображение результатов
# # Визуализация результатов
# for result in results:
#     boxes = result.boxes.xyxy  # Получаем координаты ограничивающих рамок
#     confidences = result.boxes.conf  # Получаем уверенность предсказаний
#     class_ids = result.boxes.cls  # Получаем метки классов
#
#     # Рисуем ограничивающие рамки на изображении (если используем OpenCV)
#     for box, conf, cls_id in zip(boxes, confidences, class_ids):
#         x1, y1, x2, y2 = map(int, box)  # Преобразуем координаты в int
#         label = model.names[int(cls_id)]  # Получаем имя класса
#         score = float(conf)  # Получаем уверенность предсказания
#
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(image, f"{label} {score:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
# # Отображаем изображение с предсказаниями с помощью OpenCV
# cv2.imshow('Predictions', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Если нужно отобразить результат в Jupyter Notebook, можно сделать следующее:
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')  # Убираем оси для красоты
# plt.show()


import cv2
from ultralytics import YOLO

# Загрузка обученной модели
model = YOLO('/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/AI_microservice/runs/detect/train2/weights/best.pt')

# Загрузка изображения
image = cv2.imread('/home/devu/PycharmProjects/aplicationForTheCompanyAndPartners/AI_microservice/runs/detect/train2/val_batch0_pred.jpg')

# Выполнение предсказания
results = model.predict(image)

# Визуализация предсказаний
for result in results:
    plotted_image = result.plot()
    cv2.imshow('YOLOv8 Inference', plotted_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
