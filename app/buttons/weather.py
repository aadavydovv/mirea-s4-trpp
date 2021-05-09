class ButtonWeather:
    @staticmethod

    def action(country):

        '''
        Returns formatted string with weather

        Returns formatted string with weather from Aeris API.
        The location is determined by passing the country code to the function.

        :param country: string
            code of country from where the weather will be shown
        :return: string
            formatted string
        '''

        import requests

        #cretaing request to AerisAPI
        if country == 'de':
            weather_string = 'Tommorow in Berlin: '
            request_result = requests.post('https://api.aerisapi.com/forecasts/berlin,de?filter=1d&limit=10&fields=periods.maxTempC,periods.weatherPrimary&client_id=YA2U5w6PHL8Z4MRkHLEeY&client_secret=lsb5pqlmCJEuNVkzvs4AwEVCkiWU14RdjFhUFOZX')

        elif country == 'ru':
            weather_string = 'Tommorow in Moscow: '
            request_result = requests.post('https://api.aerisapi.com/forecasts/moscow,ru?filter=1d&limit=10&fields=periods.maxTempC,periods.weatherPrimary&client_id=YA2U5w6PHL8Z4MRkHLEeY&client_secret=lsb5pqlmCJEuNVkzvs4AwEVCkiWU14RdjFhUFOZX')

        #writes request as JSON-encoded content of responce
        request_result = request_result.json()

        #checking the correctness of the query result
        if request_result['success'] == True:
            for request_response in request_result['response']:

                #getting dict that contains weather forecast for next day
                weather = request_response['periods'][0]

                weather_tempC = str(weather['maxTempC'])
                weather_status = weather['weatherPrimary']

                weather_string = weather_string + weather_status + ' ' + weather_tempC + 'C°'

                return weather_string
