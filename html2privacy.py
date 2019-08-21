import html2text
import nltk
import urllib
from bs4 import BeautifulSoup
from bs4 import Comment
import re

start_urls = []
with open("./set/privacy_policy_url.txt", "r", encoding="utf-8") as rfile:
    for f in rfile:
        url = f.strip()
        start_urls.append(url)

h = html2text.HTML2Text()
h.ignore_links = True

for url in start_urls:
    name = str(url.split('/')[2])

    with open("./privacy_policy/"+name+".html", "r", encoding="utf-8") as fin:
        html = fin.read()
    # html = urllib.request.urlopen(url)
        h_txt = h.handle(str(html))

        with open('./html2txt/' +name + '.md', 'w', encoding="utf-8") as f:
            f.write(str(h_txt) + '\n')
        #
        # nltk_txt = nltk.clean_html(html)
        # with open('./nltk2txt/' + name + '.txt', 'w', encoding="utf-8") as f:
        #     f.write(str(nltk_txt) + '\n')

        soup = BeautifulSoup(html)
        [x.extract() for x in soup.find_all('script')]
        [x.extract() for x in soup.find_all('style')]
        [x.extract() for x in soup.find_all('meta')]
        [x.extract() for x in soup.find_all('noscript')]
        [x.extract() for x in soup.find_all(text=lambda text: isinstance(text, Comment))]

        b_text = soup.get_text()

        b_text = re.sub('\s+', ' ', b_text)
        lines = (line.strip() for line in b_text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        b_text = '\n'.join(chunk for chunk in chunks if chunk)

        with open('./bs42txt/' + name + '.txt', 'w', encoding="utf-8") as f:
            f.write(str(b_text) + '\n')
