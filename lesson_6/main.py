import json
import requests
from bs4 import BeautifulSoup
import re


def get_page_data(url: str) -> str:
    response = requests.get(url, headers={
        # like human
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/130.0.0.0 Safari/537.36'
    })

    if response.ok:
        return response.text
    else:
        # pass error to some log
        return ''


def get_news_bbc(html: str) -> dict|list:
    soup = BeautifulSoup(html, 'html.parser')

    main_content = soup.find(id='main-content')
    ul_tag = main_content.find('ul', {'role': 'list', 'class': re.compile(r'^ssrcss-')})

    res = []
    if ul_tag:
        articles = ul_tag.find_all('div', {'type': 'article'}, limit=5)
        for article in articles:
            link = 'https://www.bbc.com'+article.find('a').get('href')

            topics = []
            htmlSinglePage = get_page_data(link)
            if htmlSinglePage:
                topics = get_topic_bbc(htmlSinglePage)

            res.append({
                'link': link,
                'topics': topics
            })

    return res


def get_topic_bbc(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')

    wrap = soup.find('div', {'data-component': 'topic-list'})
    ul = wrap.find('ul', {'role': 'list'})
    topics = ul.find_all('a')

    res = []
    for topic in topics:
        res.append(topic.get_text())

    return res


def save_to_json(data: dict) -> None:
    with open('out_data.json', 'w', encoding='utf-8') as out:
        json.dump(data, out, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    html = get_page_data(' https://www.bbc.com/sport')
    all_data = get_news_bbc(html)
    save_to_json(all_data)

    print('Done')
