class ButtonNews:
    @staticmethod
    def action(country):
        import requests

        # https://newsapi.org/v2/top-headlines?country=ru&apiKey=7bc1b015bc614813ad32a62accce3cd1

        if country == 'ru':
            request_result = requests.get(
                'https://newsapi.org/v2/top-headlines?country=ru&apiKey=7bc1b015bc614813ad32a62accce3cd1')

        elif  country == 'de':
            request_result = requests.get('https://newsapi.org/v2/top-headlines?country=de&apiKey=7bc1b015bc614813ad32a62accce3cd1')

        request_result = request_result.json()

        output_string = ''

        if request_result['status'] == 'ok':
            for i in range(5):
                article = request_result['articles'][i]
                headline = '   ' + article['title']
                # print(output_string)
                output_string = output_string + "\n" + headline

        return output_string