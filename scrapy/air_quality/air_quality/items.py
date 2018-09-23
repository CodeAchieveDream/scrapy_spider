# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirQualityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_name = scrapy.Field()        # 城市名称
    record_data = scrapy.Field()      # 检测日期
    aqi_val = scrapy.Field()          # AQI
    range_val = scrapy.Field()        # 范围
    quality_level = scrapy.Field()    # 质量等级
    pm2_5_val = scrapy.Field()        # PM2.5
    pm10_val = scrapy.Field()         # PM10
    so2_val = scrapy.Field()          # SO2
    co_val = scrapy.Field()           # CO
    no2_val = scrapy.Field()          # NO2
    o3_val = scrapy.Field()           # O3
    rank = scrapy.Field()             # 排名

