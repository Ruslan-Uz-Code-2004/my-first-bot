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


def get_news_pagination():
    news_article_href = []
    for i in range(31):
        s = requests.Session()
        respanse = s.get(
            url=f'https://hi-tech.news/page/{i}/', headers=headers)
        soup = BeautifulSoup(respanse.text, 'lxml')
        article_urls = soup.find_all('a', class_='post-title-a')
        for url in article_urls:
            news_href = url.get('href')
            news_article_href.append(news_href)
            time.sleep(randrange(2, 4))
        with open('index.txt', 'w', encoding='utf-8') as file:
            for url in news_article_href:
                file.write(f'{url}\n')


def get_news_data():
    with open('index.txt') as file:
        urls_list = [line.strip() for line in file.readlines()]

    s = requests.Session()
    result_data = []

    for url in urls_list:
        response = s.get(url=url, headers=headers)
        time.sleep(randrange(5, 12))

        soup = BeautifulSoup(response.text, 'lxml')
        article_content = soup.find('h1', class_='title').text.strip()
        article_news_data = soup.find(
            'div', class_='tile-views').text.strip()
        article_text = soup.find(
            'div', class_='post-content').find('div', class_='the-excerpt').text.strip()

        result_data.append({
            'article_title': article_content,
            'article_data': article_news_data,
            'article_text': article_text,
            'article_urls': url
        })

    with open('result_information.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def main():
    # get_news_pagination()
    get_news_data()


if __name__ == '__main__':
    main()
