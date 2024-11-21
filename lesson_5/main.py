import json
import sqlite3
import requests
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


def parce_html(html_in: str) -> dict:
    pattern_articles = r'<article[^>]*\bclass=["\'][^"\']*\bjob\b[^"\']*["\'][^>]*>(.*?)</article>'
    articles = re.findall(pattern_articles, html_in, re.DOTALL)

    pattern_title = r'<h3\s+class="[^"]*\bjobCard_title\b[^"]*\s+m-0"[^>]*>(.*?)</h3>'
    pattern_url = r'<a [^>]*href=["\'](https?://[^"\']+)["\'][^>]*>'

    res = []
    for idx, article in enumerate(articles):
        title = ''.join(re.findall(pattern_title, article))
        url = ''.join(re.findall(pattern_url, article))

        res.append(dict(title=title, url=url))

    return res


def save_to_json(data: dict) -> None:
    with open('out_data.json', 'w', encoding='utf-8') as out:
        json.dump(data, out, ensure_ascii=False, indent=4)


def save_to_sql_lite(data: dict) -> None:
    # todo:
    print('')


if __name__ == '__main__':
    html = get_page_data('https://www.lejobadequat.com/emplois')
    res = parce_html(html)

    save_to_json(res)

    print('Done')
