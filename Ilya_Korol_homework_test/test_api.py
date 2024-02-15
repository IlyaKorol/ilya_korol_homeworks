# Необходимо к полученным вами ответам от API, написать тесты. Данные тесты должны
# содержать проверки: статус код, содержимое результата(получить значение и его сравнить),
# можно проверить заголовки и т.д.

import requests

class TestMain:
    def test_one(self):
        params = {'q': 'python'}
        response = requests.get('https://www.google.com/search', params=params)
        print(response.status_code)
        assert response.status_code == 200, 'Error 200'  # Проверка на статус-код
    def test_two(self):
        params = {'q': 'python'}
        response = requests.get('https://www.google.com/search', params=params)
        print(response.headers)
        assert response.headers['Content-Type'] == 'text/html; charset=utf-8'  # Проверка заголовка
    def test_three(self):
        params = {'q': 'python'}
        response = requests.get('https://www.google.com/search', params=params)
        print(response.text)
        html_text = response.text
        with open('html_google.html', 'w') as file:
            file.write(html_text)
        assert len(response.text) > 10000
