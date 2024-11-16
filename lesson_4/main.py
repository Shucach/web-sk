import requests
import re


def get_page_data(url: str) -> str:
    response = requests.get(url, headers={
        # like human
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/130.0.0.0 Safari/537.36'
    })

    if response.status_code == 200:
        return response.text
    else:
        # pass error to some log
        return ''


def parce_html(html_in: str) -> list:
    pattern = r'<h3\s+class="[^"]*\bjobCard_title\b[^"]*\s+m-0"[^>]*>(.*?)</h3>'
    res = re.findall(pattern, html_in)

    return res


if __name__ == '__main__':
    html = get_page_data('https://www.lejobadequat.com/emplois')
    titles = parce_html(html)
    print(titles)