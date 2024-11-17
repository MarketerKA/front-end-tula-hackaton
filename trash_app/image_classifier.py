from roboflow import Roboflow

# Подключение к Roboflow
VERSION=1
rf = Roboflow(api_key="d6PoPvkjGCOvvPkoMxJB")
project = rf.workspace().project("garbage-containers-ntlho")
model = project.version(VERSION).model  # Укажите версию вашей модели

# Функция для предсказания изображения
def predict_image(image_path):
    response = model.predict(image_path, confidence=40, overlap=30).json()  # Предсказание
    predictions = response.get("predictions", [])  # Достаем предсказания

    # Обработка предсказаний
    for prediction in predictions:
        class_name = prediction.get("class", "")
        if class_name == "closed_container":
            print("Закрытый контейнер")
        elif class_name == "empty_container":
            print("Пустой контейнер")
        elif class_name == "full_container":
            print("Полный контейнер")
        elif class_name == "garbage":
            print("Мусор")
        elif class_name == "not_seen_container":
            print("Контейнер не виден полностью")
        else:
            print(f"Обнаружен объект: {class_name}")