class ButtonNews:
    @staticmethod
    def action(country):
        import requests

        #creating request to newsAPI
        if country == 'ru':
            request_result = requests.get(
                'https://newsapi.org/v2/top-headlines?country=ru&apiKey=7bc1b015bc614813ad32a62accce3cd1')

        elif country == 'de':
            request_result = requests.get('https://newsapi.org/v2/top-headlines?country=de&apiKey=7bc1b015bc614813ad32a62accce3cd1')

        #saves only json-encoded content from request
        request_result = request_result.json()

        output_string = ''

        #verifying request result
        if request_result['status'] == 'ok':
            #parsing json for 5 first headlines
            for i in range(5):
                article = request_result['articles'][i]
                headline = '   ' + article['title']
                if i != 0:
                    output_string = output_string + "\n" + headline
                else:
                    output_string = output_string + headline

        return output_string
