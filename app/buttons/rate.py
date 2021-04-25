import requests


class ButtonRate:

    # действие кнопки; возвращает строку с курсом валюты выбранной страны
    @staticmethod
    def action():

        # информацию об актуальных курсах обмена валют берем с сайта ratesapi.io
        url = 'https://api.ratesapi.io/api/latest?base=EUR'

        response = requests.get(url)
        data = response.json()
        rate = round(data['rates']['RUB'], 3)

        return f'Курс рубля к евро: {rate} RUB = 1 EUR'
