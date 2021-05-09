import requests


class ButtonRate:
    """
    Button action. Returns exchange rate statistics for two countries.
    Exchange rates are taken from ratesapi.io

    :rtype: str
    :return: Formatted string
    """
    @staticmethod
    def action():

        url = 'https://api.ratesapi.io/api/latest?base=EUR'

        response = requests.get(url)
        data = response.json()
        rate = round(data['rates']['RUB'], 3)

        return f'Курс рубля к евро: {rate} RUB = 1 EUR'
