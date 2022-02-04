from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time
from random import randrange
import json

ua = UserAgent()

headers = {'user-agent': f'{ua.random}',
           'accept': '*/*'
           }


def get_collect_data():
    article_hrefs = []
    for i in range(11):
        req = requests.get(f'https://stopgame.ru/games?p={i}', headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        article_urls = soup.find_all(
            'div', class_='caption caption-bold')
        for href in article_urls:
            article_href = href.find('a').get('href')
            article_hrefs.append(article_href)
            time.sleep(randrange(2, 4))

        with open('../index_2.txt', 'w', encoding='utf-8') as file:
            for url in article_hrefs:
                file.write(f'https://stopgame.ru{url}\n')


def get_data():
    with open('../index_2.txt') as file:
        urls_list = [line.strip() for line in file.readlines()]

    s = requests.Session()
    result_data = []

    for url in urls_list:
        response = s.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        article_title = soup.find('h1', class_='article-title').text.strip()
        result_data.append({
            'article_title': article_title,
            'article_urls': url

        })
    with open('../result_game_info.json', 'w', encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def main():
    get_collect_data()
    get_data()


if __name__ == '__main__':
    main()
