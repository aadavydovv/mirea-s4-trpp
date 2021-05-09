import requests


class ButtonCovid:

    # действие кнопки; возвращает строку со статистикой COVID-19 по выбранной стране
    @staticmethod
    def action(country):

        # актуальные данные по COVID-19 берем с сайта covid19api.com
        url_ru = 'https://api.covid19api.com/total/country/russia'
        url_de = 'https://api.covid19api.com/total/country/germany'

        output = []
        if country is "ru":
            response = requests.get(url_ru)
        else:
            response = requests.get(url_de)
        data = response.json()

        # берём последнюю известную информацию из json файла
        for key in data[-1]:
            output.append(data[-1][key])

        return f'Зарегистрировано случаев: {output[7]}\nСмертей: {output[8]}\nВыздоровело: {output[9]} \nАктивных ' \
               f'случаев: {output[10]} '