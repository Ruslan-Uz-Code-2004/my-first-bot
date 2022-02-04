# my-first-bot
Данный бот был разработан в течении недели. Он парсит данные с различных сайтов и возвращает в виде __json__. 
***
### Функционал бота:

1. Сбор данных с cs-maney.com и возврат товаров со скидкой более __10%__
2. Сбор данных с Markaziy Bank Uzb о курсе валют за 1 день в сумах
3. Парсинг новостей с сайта ___https://hi-tech.news/___ 
4. Топ 100 игр по рейтингам __StopGame__ 
***
### Требуемые библиотеки:
Для работы данный бот использует библеотеки __requests__ , __BeautifulSoup__ , __aiogram__ .
***
#### ___BeautifulSoup___ 

Для установки введите команду:
```pip install bs4```

Данная библеотека помогает нам распарсить сайты с помощью python

___Пример кода BeautifulSoup 4 ___:
```

from bs4 import BeautifulSoup
import requests as req
    
resp = req.get("http://www.something.com")
 
soup = BeautifulSoup(resp.text, 'lxml')
 
print(soup.title)
print(soup.title.text)
print(soup.title.parent)

```
Этот код парсит ланные с сайта и выводит нам нужную информацию. Ссылка на [документацию](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 
 ***
 #### requests
 
 Для установки введите команду:
```pip install requests ```

Это библеотека отправляет get() либо post() запросы на сайт

___Пример кода requests___

```
import requests

r = requests.get('https://api.github.com/events')
r.json()

```
Документация [requests](https://docs.python-requests.org/en/latest/user/quickstart/)


 
