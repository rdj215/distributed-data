# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Individual records from scraped site 
class Record(scrapy.Item):
    ward = scrapy.Field()
    division = scrapy.Field()
    position = scrapy.Field()
    elected = scrapy.Field()
    name = scrapy.Field()
    
    
