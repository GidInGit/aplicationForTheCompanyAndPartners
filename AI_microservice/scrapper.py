# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# for i in range(1, 29):
#     # URL веб-страницы, откуда нужно скачать изображения
#     url = 'https://sotni.ru/fon-stroitelnaya-kaska/'
#
#     # Папка для сохранения скачанных изображений
#     output_folder = './downloaded_images'
#     os.makedirs(output_folder, exist_ok=True)
#
#     # Получение HTML содержимого страницы
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # Поиск всех тегов <img> на странице
#     img_tags = soup.find_all('img')
#
#     # Скачивание и сохранение изображений
#     for img in img_tags:
#         img_url = img.get('src')
#         if not img_url:
#             continue
#         # Приведение относительных URL к абсолютным
#         img_url = urljoin(url, img_url)
#
#         # Получение имени файла из URL
#         img_name = os.path.basename(img_url)
#
#         # Скачивание изображения
#         img_response = requests.get(img_url)
#         if img_response.status_code == 200:
#             img_path = os.path.join(output_folder, img_name)
#             with open(img_path, 'wb') as f:
#                 f.write(img_response.content)
#             print(f"Скачано: {img_name}")
#         else:
#             print(f"Не удалось скачать: {img_name}")
#
#     print("Все изображения скачаны.")

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# URL веб-страницы, откуда нужно скачать изображения
url = 'https://sotni.ru/fon-stroitelnaya-kaska/'

# Папка для сохранения скачанных изображений
output_folder = './downloaded_images'
os.makedirs(output_folder, exist_ok=True)

# Получение HTML содержимого страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Поиск всех тегов <img> на странице
img_tags = soup.find_all('img')

# Скачивание и сохранение изображений
for img in img_tags:
    img_url = img.get('src')
    if not img_url:
        continue

    # Пропуск data URL
    if img_url.startswith('data:'):
        continue

    # Приведение относительных URL к абсолютным
    img_url = urljoin(url, img_url)

    # Проверка, что URL начинается с http или https
    parsed_url = urlparse(img_url)
    if parsed_url.scheme not in ('http', 'https'):
        continue

    # Получение имени файла из URL
    img_name = os.path.basename(parsed_url.path)

    # Скачивание изображения
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        img_path = os.path.join(output_folder, img_name)
        with open(img_path, 'wb') as f:
            f.write(img_response.content)
        print(f"Скачано: {img_name}")
    else:
        print(f"Не удалось скачать: {img_name}")

print("Все изображения скачаны.")
