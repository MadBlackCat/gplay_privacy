  # -*- coding: utf-8 -*-
import scrapy
import time
import html2text
import nltk
import urllib
from bs4 import BeautifulSoup
import sys
from bs4 import Comment
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import re
from scrapy.spiders import CrawlSpider, Rule


class PrivacyPolicySpider(CrawlSpider):

    name = "privacy"

    def start_requests(self):
        urls = []
        with open("./set/privacy_policy_url.txt", "r", encoding="utf-8") as rfile:
            for f in rfile:
                url = f.strip()
                urls.append(url)
        for ele in urls:
            yield scrapy.Request(url = ele, callback=self.parse_privacy)
        # url = "http://shared.youdao.com/dict/market/youdaoInc/index.html#/EN"
        # yield scrapy.Request(url=url, callback = self.parse_privacy)

    def __init__(self):
        # 浏览器 selenium 配置

        # Firefox
        # firefox_profile = webdriver.FirefoxProfile()
        # firefox_profile.set_preference("permissions.default.image",2)
        # firefox_profile.set_preference("int1.accept_language", "en-GB")
        # firefox_profile.update_preferences()
        # self.driver = webdriver.Firefox(firefox_profile)

        # Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=en-US')
        # chrome_options.add_argument('--proxy-server=http://174.138.46.194:8080')
        prefs = {"profile.managed_default_content_settings.images":2, "int1.accept_language": "en-GB"}
        chrome_options.add_experimental_option('prefs',prefs)
        self.driver = webdriver.Chrome(chrome_options = chrome_options)

    def parse_privacy(self, response):

        self.driver.get(response.url)
        time.sleep(10)
        html_selennium_text = self.driver.find_elements_by_xpath("//body")[0].text

        html = self.driver.page_source
        name = str(response.url.split('/')[2].split(':')[0])
        with open('./selen_text/' + name + '.md', 'w', encoding="utf-8") as f:
            f.write(str( html_selennium_text))

        h = html2text.HTML2Text()
        h.ignore_links = True
        h_txt = h.handle(str(html))
        with open('./html2txt/' + name + '.md', 'w', encoding="utf-8") as f:
            f.write(str(h_txt))
        #
        # nltk_txt = nltk.clean_html(html)
        # with open('./nltk2txt/' + name + '.txt', 'w', encoding="utf-8") as f:
        #     f.write(str(nltk_txt) + '\n')

        soup = BeautifulSoup(html, "lxml")
        [x.extract() for x in soup.find_all('script')]
        [x.extract() for x in soup.find_all('style')]
        [x.extract() for x in soup.find_all('meta')]
        [x.extract() for x in soup.find_all('noscript')]
        [x.extract() for x in soup.find_all(text=lambda text: isinstance(text, Comment))]

        b_text = soup.get_text()

        b_text.replace('\\n', ' ').replace('\\t', ' ')
        b_text = re.sub('\s+', ' ', b_text)
        with open('./bs42txt/' + name + '.txt', 'w', encoding="utf-8") as f:
            f.write(str(b_text))

        # privacy_policy = response.xpath(
        #     '//div[contains(text(),"Developer")]/..//a[contains(text(),"Privacy Policy")]/@href').extract()
        # privacy_policy = privacy_policy[0] if len(privacy_policy) > 0 else "Error : " + str(url)

        with open('./privacy_policy/'+name+'.html', 'w', encoding="utf-8") as f:
            f.write(str(html))







