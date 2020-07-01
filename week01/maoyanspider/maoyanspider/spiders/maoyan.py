# -*- coding: utf-8 -*-
import scrapy
from maoyanspider.items import  MaoyanspiderItem
from scrapy.selector import Selector,SelectorList

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    def parse(self,response):
        item = MaoyanspiderItem()
        item_list = Selector(response=response).xpath('//div[@class="movie-item-hover"]')
        for item_info in item_list[:10]:
            movie_name = item_info.xpath('./a/div/div[1]/span[1]/text()').extract() [0]
            movie_tag = item_info.xpath('./a/div/div[2]/text()'.extract()[1].strip('\n'))
            movie_time = item_info.xpath('./a/div/div[4]/text()'.extract()[1].strip('\n'))
            movie_link = item_info.xpath('./a/@href').get()
            item['movie_name'] = movie_name
            item['movie_tag'] = movie_tag
            item['movie_time'] = movie_time
            item['movie_link'] = "htttps://maoyan.com" + movie_link
            print(item)
            yield item


