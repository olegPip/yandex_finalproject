# Олег Цыбулин, 20-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data


# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data

order_response = post_new_order(data.order_body)


# Запрос на получение заказа по треку заказа
def get_order(track_order):
    return requests.get(configuration.URL_SERVICE+configuration.PUT_ORDER,
                        params=track_order)
