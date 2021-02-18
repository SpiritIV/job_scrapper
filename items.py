# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field()
    salary_from = scrapy.Field()
    salary_to = scrapy.Field()
    link_vac = scrapy.Field()
    link_site = scrapy.Field()

    pass