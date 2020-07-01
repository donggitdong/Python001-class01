# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_tag = item['movie_tag']
        movie_time = item['movie_time']
        movie_link = item['movie_link']
        output = [f'movie_name: {movie_name.strip()} movie_tag: {movie_tag.strip()} movie_time: {movie_time.strip()} movie_link: {movie_link.strip()}']
        print('------begin print------')
        print(output)
        print('-------end print--------')
        movie_save_data = pd.DataFrame(data=output)
        movie_save_data.to_csv('../scrapy_spider_movie_data.csv',mode='a',index=False,encoding='utf-8',header=False)
        return item

    
