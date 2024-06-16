import face_recognition
import cv2
import numpy as np
import psycopg2
import pickle


# Подключение к базе данных PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname="face_recognition_db",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )


# Загрузка лиц из базы данных
def load_known_faces():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, face_encoding FROM known_faces")
    known_face_encodings = []
    known_face_names = []

    for row in cursor.fetchall():
        name, face_encoding = row
        face_encoding = pickle.loads(face_encoding)
        known_face_names.append(name)
        known_face_encodings.append(face_encoding)

    cursor.close()
    conn.close()

    return known_face_encodings, known_face_names


# Загрузка лиц из базы данных
known_face_encodings, known_face_names = load_known_faces()

# Захват видео с камеры
video_capture = cv2.VideoCapture(0)

while True:
    # Захват кадра
    ret, frame = video_capture.read()

    # Преобразование кадра из BGR в RGB
    rgb_frame = frame[:, :, ::-1]

    # Обнаружение лиц и получение их кодировок
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Сравнение каждого лица с известными лицами
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Выбор самого близкого совпадения
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    # Отображение результатов
    for (top, right, bottom, left), name in zip(face_locations, face_names):
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
