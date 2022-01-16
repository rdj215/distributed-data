import scrapy
from crawler.items import Record 
# from scrapy.spiders import Rule, CrawlSpider
# from scrapy.linkextractors import LinkExtractor



class PhiladelphiavotesSpider(scrapy.Spider):
    name = 'philadelphiavotes'
    allowed_domains = ['philadelphiavotes.com']
    start_urls = ['http://philadelphiavotes.com/en/election-board-officials/current-election-board-officials.html']

    # Scrapes data from Current Election Board Table and creates an array of dict records
    def parse(self, response):
        record_array =[]
        record = Record()
        record['ward'] = response.xpath('//td[@class="cell0"]/text()').getall()
        record['division'] = response.xpath('//td[@class="cell1"]/text()').getall()
        record['position'] = response.xpath('//td[@class="cell2"]/text()').getall()
        record['elected'] = response.xpath('//td[@class="cell3"]/text()').getall()
        record['name'] = response.xpath('//td[@class="cell4"]/text()').getall()

        for i in range(len(record['name'])):
            record_array.append({"ward":record['ward'][i], "division":record['division'][i], 'position':record['position'][i], 'elected':record['elected'][i], 'name':record['name'][i]})

        return record_array 


       



