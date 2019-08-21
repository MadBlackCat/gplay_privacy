  # -*- coding: utf-8 -*-
import scrapy
import time

import sys

from scrapy.spiders import CrawlSpider, Rule


class GooglePrivacySpider(CrawlSpider):

    name = "google_privacy"

    start_urls = []
    with open("./set/hot_url.txt", "r", encoding="utf-8") as rfile:
        for f in rfile:
            url = 'https://play.google.com' + f.strip()
            start_urls.append(url)

    # def start_requests(self):
    #
    #
    #
    #     for ele in urls:
    #
    #         yield scrapy.Request(url=ele, callback=self.parse_app)

    def parse(self, response):

        url = response.url
        privacy_policy = response.xpath(
            '//div[contains(text(),"Developer")]/..//a[contains(text(),"Privacy Policy")]/@href').extract()
        privacy_policy = privacy_policy[0] if len(privacy_policy) > 0 else "Error : " + str(url)

        with open('./set/privacy_policy_url.txt', 'a+', encoding="utf-8") as f:
            f.write(str(privacy_policy) + '\n')







