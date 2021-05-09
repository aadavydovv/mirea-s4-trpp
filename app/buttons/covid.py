import requests


class ButtonCovid:
    @staticmethod
    def action(country):
        """
        Button action. Returns COVID-19 statistics by country.
        COVID-19 statistics are taken from covid19api.com

        :param country: country code

        :rtype: str
        :return: Formatted string
        """
        url_ru = 'https://api.covid19api.com/total/country/russia'
        url_de = 'https://api.covid19api.com/total/country/germany'

        output = []
        if country is "ru":
            response = requests.get(url_ru)
        else:
            response = requests.get(url_de)
        data = response.json()

        # take latest info from json file
        for key in data[-1]:
            output.append(data[-1][key])

        return f'Зарегистрировано случаев: {output[7]}\nСмертей: {output[8]}\nВыздоровело: {output[9]} \nАктивных ' \
               f'случаев: {output[10]} '
