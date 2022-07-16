import bs4
import requests


KEYWORDS = ['дизайн', 'фото', 'web', 'python',
            'GitLab', 'Reddit', 'Хабр', 'Javascript', 'Rust']

HEADERS = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
           'Cache-Control': 'max-age=0', 'DNT': '1', 'Referer': 'https://google.com', 'Pragma': 'no-cache'}
HUBS = ['JavaScript', 'Java', 'Старое железо']

base_url = 'http://habr.com'
url = base_url+'/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    date = article.find("time").attrs['title']
    title = article.find("h2").find("span").text
    href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
    news = article.find_all(
        class_="tm-article-body tm-article-snippet__lead")
    for i in news:
        resulting_list = [j.text for j in i if j != ' ']
        resulting_list = str(resulting_list)
        for el in KEYWORDS:
            if el in resulting_list:
                print(
                    f'ДАТА ПУБЛИКАЦИИ <{date}> / ЗАГОЛОВОК <{title}> / ССЫЛКА <{base_url+href}>\n' + "----"*20)
