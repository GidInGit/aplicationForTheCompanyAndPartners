# import face_recognition
# import cv2
# import numpy as np
# import psycopg2
# import pickle
#
#
# # Подключение к базе данных PostgreSQL
# def connect_db():
#     return psycopg2.connect(
#         dbname="face_recognition_db",
#         user="your_username",
#         password="your_password",
#         host="your_host",
#         port="your_port"
#     )
#
#
# # Загрузка лиц из базы данных
# def load_known_faces():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, face_encoding FROM known_faces")
#     known_face_encodings = []
#     known_face_names = []
#
#     for row in cursor.fetchall():
#         name, face_encoding = row
#         face_encoding = pickle.loads(face_encoding)
#         known_face_names.append(name)
#         known_face_encodings.append(face_encoding)
#
#     cursor.close()
#     conn.close()
#
#     return known_face_encodings, known_face_names
#
#
# # Загрузка лиц из базы данных
# known_face_encodings, known_face_names = load_known_faces()
#
# # Захват видео с камеры
# video_capture = cv2.VideoCapture(0)
#
# while True:
#     # Захват кадра
#     ret, frame = video_capture.read()
#
#     # Преобразование кадра из BGR в RGB
#     rgb_frame = frame[:, :, ::-1]
#
#     # Обнаружение лиц и получение их кодировок
#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#
#     # Сравнение каждого лица с известными лицами
#     face_names = []
#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"
#
#         # Выбор самого близкого совпадения
#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         best_match_index = np.argmin(face_distances)
#         if matches[best_match_index]:
#             name = known_face_names[best_match_index]
#
#         face_names.append(name)
#
#     # Отображение результатов
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Рисование квадрата вокруг лица
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#
#         # Рисование имени под лицом
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#     # Отображение кадра
#     cv2.imshow('Video', frame)
#
#     # Прерывание цикла по нажатию клавиши 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Освобождение захвата и закрытие всех окон
# video_capture.release()
# cv2.destroyAllWindows()



# import face_recognition
# import cv2
# import numpy as np
#
# # Функция для загрузки и кодирования изображений
# def load_and_encode_image(file_path):
#     try:
#         image = face_recognition.load_image_file(file_path)
#         encodings = face_recognition.face_encodings(image)
#         if len(encodings) > 0:
#             return encodings[0]
#         else:
#             print(f"Лицо не найдено на изображении: {file_path}")
#             return None
#     except Exception as e:
#         print(f"Ошибка при обработке изображения {file_path}: {e}")
#         return None
#
#
# # Пример предопределенных лиц (вместо загрузки из базы данных)
# person_1_encodings = [
#     load_and_encode_image("photo_5435882134087786880_y.jpg"),
#     load_and_encode_image("photo_5435882134087786881_y.jpeg"),
#     load_and_encode_image("photo_5435882134087786883_y.jpeg")
# ]
# person_2_encodings = [
#     load_and_encode_image("danil_jmurik_1.jpeg"),
#     load_and_encode_image("danil_jmurik_2.jpeg"),
#     load_and_encode_image("danil_jmurik_3.jpeg")
# ]
# person_3_encodings = [
#     load_and_encode_image("danil_jmurik_1.jpeg"),
#     load_and_encode_image("danil_jmurik_2.jpeg"),
#     load_and_encode_image("danil_jmurik_3.jpeg")
# ]
#
# # Удаление None значений из списка
# person_1_encodings = [enc for enc in person_1_encodings if enc is not None]
# person_3_encodings = [enc for enc in person_3_encodings if enc is not None]
#
#
# known_face_encodings = {
#     "Maks": person_1_encodings,
#     "Danil": person_3_encodings,
#
# }
#
# # Проверка, что лица были успешно загружены и закодированы
# for name, encodings in known_face_encodings.items():
#     if len(encodings) == 0:
#         print(f"Не удалось загрузить кодировки для {name}")
#
# # Захват видео из файла
# video_capture = cv2.VideoCapture('danil.mp4')
#
# while video_capture.isOpened():
#     # Захват кадра
#     ret, frame = video_capture.read()
#     if not ret:
#         break
#
#     # Преобразование кадра из BGR в RGB
#     rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])
#
#     # Обнаружение лиц и получение их кодировок
#     face_locations = face_recognition.face_locations(rgb_frame)
#     if len(face_locations) == 0:
#         print("Лицо не обнаружено в текущем кадре")
#         continue
#
#     # Получение кодировок лиц
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#     if len(face_encodings) == 0:
#         print("Не удалось получить кодировки лиц в текущем кадре")
#         continue
#
#     # Сравнение каждого лица с известными лицами
#     face_names = []
#     for face_encoding in face_encodings:
#         name = "Unknown"
#         min_distance = float("inf")
#
#         # Проверка каждой кодировки лица против всех известных лиц
#         for known_name, encodings in known_face_encodings.items():
#             if not encodings:
#                 continue
#             matches = face_recognition.compare_faces(encodings, face_encoding)
#             face_distances = face_recognition.face_distance(encodings, face_encoding)
#
#             # Найти минимальное расстояние и соответствующее имя
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index] and face_distances[best_match_index] < min_distance:
#                 min_distance = face_distances[best_match_index]
#                 name = known_name
#
#         face_names.append(name)
#
#     # Отображение результатов
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Рисование квадрата вокруг лица
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#
#         # Рисование имени под лицом
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#     # Отображение кадра
#     cv2.imshow('Video', frame)
#
#     # Прерывание цикла по нажатию клавиши 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Освобождение захвата и закрытие всех окон
# video_capture.release()
# cv2.destroyAllWindows()




import face_recognition
import cv2
import numpy as np

# Функция для загрузки и кодирования изображений
def load_and_encode_image(file_path):
    try:
        image = face_recognition.load_image_file(file_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            return encodings[0]
        else:
            print(f"Лицо не найдено на изображении: {file_path}")
            return None
    except Exception as e:
        print(f"Ошибка при обработке изображения {file_path}: {e}")
        return None
person_1_encodings = [
    load_and_encode_image("photo_5435882134087786880_y.jpg"),
    load_and_encode_image("photo_5435882134087786881_y.jpeg"),
    load_and_encode_image("photo_5435882134087786883_y.jpeg")
]
person_2_encodings = [
    load_and_encode_image("danil_1.jpeg"),
    load_and_encode_image("danil_2.jpeg"),
    load_and_encode_image("danil_3.jpeg")
]
person_3_encodings = [
    load_and_encode_image("danil_jmurik_1.jpeg"),
    load_and_encode_image("danil_jmurik_2.jpeg"),
    load_and_encode_image("danil_jmurik_3.jpeg")
]
# Удаление None значений из списка
person_1_encodings = [enc for enc in person_1_encodings if enc is not None]
person_2_encodings = [enc for enc in person_2_encodings if enc is not None]
person_3_encodings = [enc for enc in person_3_encodings if enc is not None]

known_face_encodings = {
    "Maks": person_1_encodings,
    "JMURIK!!!!!!": person_3_encodings,
    "Danil": person_2_encodings,
}



# Захват видео с веб-камеры
video_capture = cv2.VideoCapture(0)
prev_names = set()

frame_count = 0

while video_capture.isOpened():
    # Захват кадра
    ret, frame = video_capture.read()
    if not ret:
        print("Не удалось получить кадр с веб-камеры")
        break

    # Уменьшение размера кадра для ускорения обработки
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Преобразование кадра из BGR в RGB
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

    # Обработка каждого второго кадра
    if frame_count % 2 == 0:
        # Обнаружение лиц и получение их кодировок
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = set()
        for face_encoding in face_encodings:
            name = "Unknown"
            min_distance = float("inf")

            # Проверка каждой кодировки лица против всех известных лиц
            for known_name, encodings in known_face_encodings.items():
                if not encodings:
                    continue
                matches = face_recognition.compare_faces(encodings, face_encoding)
                face_distances = face_recognition.face_distance(encodings, face_encoding)

                # Найти минимальное расстояние и соответствующее имя
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index] and face_distances[best_match_index] < min_distance:
                    min_distance = face_distances[best_match_index]
                    name = known_name
                    print(name)

            face_names.add(name)

    frame_count += 1

    # Отображение результатов
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Восстановление размера координат лица
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        # Рисование квадрата вокруг лица
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Рисование имени под лицом
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Отображение кадра
    cv2.imshow('Video', frame)

    # Прерывание цикла по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение захвата и закрытие всех окон
video_capture.release()
cv2.destroyAllWindows()


# import face_recognition
# import cv2
# import numpy as np
#
# # Функция для загрузки и кодирования изображений
# def load_and_encode_image(file_path):
#     try:
#         image = face_recognition.load_image_file(file_path)
#         encodings = face_recognition.face_encodings(image)
#         if len(encodings) > 0:
#             return encodings[0]
#         else:
#             print(f"Лицо не найдено на изображении: {file_path}")
#             return None
#     except Exception as e:
#         print(f"Ошибка при обработке изображения {file_path}: {e}")
#         return None
#
# person_1_encodings = [
#     load_and_encode_image("photo_5435882134087786880_y.jpg"),
#     load_and_encode_image("photo_5435882134087786881_y.jpeg"),
#     load_and_encode_image("photo_5435882134087786883_y.jpeg")
# ]
# person_2_encodings = [
#     load_and_encode_image("danil_1.jpeg"),
#     load_and_encode_image("danil_2.jpeg"),
#     load_and_encode_image("danil_3.jpeg")
# ]
# person_3_encodings = [
#     load_and_encode_image("danil_jmurik_1.jpeg"),
#     load_and_encode_image("danil_jmurik_2.jpeg"),
#     load_and_encode_image("danil_jmurik_3.jpeg")
# ]
# # Удаление None значений из списка
# person_1_encodings = [enc for enc in person_1_encodings if enc is not None]
# person_2_encodings = [enc for enc in person_2_encodings if enc is not None]
# person_3_encodings = [enc for enc in person_3_encodings if enc is not None]
#
# known_face_encodings = {
#     "Maks": person_1_encodings,
#     "JMURIK!!!!!!": person_3_encodings,
#     "Danil": person_2_encodings,
# }
#
# # Захват видео с веб-камеры
# video_capture = cv2.VideoCapture(0)
#
# previous_face_locations = []
# previous_face_names = []
#
# while video_capture.isOpened():
#     # Захват кадра
#     ret, frame = video_capture.read()
#     if not ret:
#         print("Не удалось получить кадр с веб-камеры")
#         break
#
#     # Уменьшение размера кадра для ускорения обработки
#     small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#
#     # Преобразование кадра из BGR в RGB
#     rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
#
#     # Обнаружение лиц и получение их кодировок только если изменилось количество лиц
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     if len(face_locations) != len(previous_face_locations):
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#         face_names = []
#         for face_encoding in face_encodings:
#             name = "Unknown"
#             min_distance = float("inf")
#
#             # Проверка каждой кодировки лица против всех известных лиц
#             for known_name, encodings in known_face_encodings.items():
#                 if not encodings:
#                     continue
#                 matches = face_recognition.compare_faces(encodings, face_encoding)
#                 face_distances = face_recognition.face_distance(encodings, face_encoding)
#
#                 # Найти минимальное расстояние и соответствующее имя
#                 best_match_index = np.argmin(face_distances)
#                 if matches[best_match_index] and face_distances[best_match_index] < min_distance:
#                     min_distance = face_distances[best_match_index]
#                     name = known_name
#                     print(name)
#
#             face_names.append(name)
#
#         previous_face_locations = face_locations
#         previous_face_names = face_names
#     else:
#         face_locations = previous_face_locations
#         face_names = previous_face_names
#
#     # Отображение результатов
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Восстановление размера координат лица
#         top *= 2
#         right *= 2
#         bottom *= 2
#         left *= 2
#
#         # Рисование квадрата вокруг лица
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#
#         # Рисование имени под лицом
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#     # Отображение кадра
#     cv2.imshow('Video', frame)
#
#     # Прерывание цикла по нажатию клавиши 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Освобождение захвата и закрытие всех окон
# video_capture.release()
# cv2.destroyAllWindows()
#

