import requests



# URL сервиса 1С
url = "http://127.0.0.1/dsa/hs/api/createlogs"

# Данные для отправки (список оборудования)
data = [
    {
        "user": "root",
        "interact": "тест",
        "target": "user",
        "data" : "1337"
    }
]

# Формируем заголовки
headers = {
    "Content-Type": "application/json",
}

# Отправляем POST-запрос
try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # Проверяем на ошибки
    
    print("Успешно отправлено!")
    print("Статус код:", response.status_code)
    print("Ответ сервера:", response.text)
    
except requests.exceptions.RequestException as e:
    print("Ошибка при отправке запроса:", e)