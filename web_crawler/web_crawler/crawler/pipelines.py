# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# remove carriage return and new line chars from record.name, convert ward and division to integers 
class StringProccessorPipeline:
    def process_item(self, record, spider):
        record['name'] = record['name'].replace('\r\n', '').strip()
        record['ward'] = int(record['ward'])
        record['division'] = int(record['division'])
        return record 
