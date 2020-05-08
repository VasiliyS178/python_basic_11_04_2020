import requests

# Свой класс ошибок для помощи другим разработчикам с тем, чтобы разобраться с ошибками
class MyError(Exception):
    def __init__(self, text=""):
        self.text = text


def some():
    raise MyError("My error text")


try:
    a = some()
except MyError as e:
    print(e)

# pip list - просмотр установленных библиотек
# pip install requests - установка библиотеки request
# python -m pip install --upgrade pip - обновление версии pip при получении рекомндации обновиться


class Product:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return getattr(self, "name")


class SpecialOfferCatalog:
    headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Version/13.1 Safari/605.1.15'}

    def __init__(self, url: str):
        self.__url = url
        self.__products = []
        self.__parse()

    def __parse(self):
        url = self.__url
        while url:
            response = requests.get(url, headers=self.headers)
            data = response.json()
            url = data["next"]
            self.__products.extend([Product(**itm) for itm in data["results"]])


url = "https://5ka.ru/api/v2/special_offers/"
catalog = SpecialOfferCatalog(url)
print(catalog)