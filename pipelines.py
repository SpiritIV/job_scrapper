# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re

class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacansy

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        i = 0
        for k in item['salary_from']:
            temp = ''
            if k == 'д':
                item['salary_to'] = re.findall('[0-9]', item['salary_from'][i + 3:])
                temp = item['salary_from'][3:i - 1]
                item['salary_from'] = temp
                break
            i += 1
        item['salary_from'] = re.findall('[0-9]', item['salary_from'])
        item['salary_from'] = ''.join(item['salary_from'])
        item['salary_to'] = ''.join(item['salary_to'])
        collection.insert_one(item)
        return item
