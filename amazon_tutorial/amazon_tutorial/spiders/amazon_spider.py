# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonTutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number=2;
    start_urls = [
        'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&lo=list&dc&fst=as%3Aoff&qid=1558356300&rnid=1250225011&ref=sr_pg_1'
                  ]

    def parse(self, response):
        items = AmazonTutorialItem()

        product_name = response.css(".a-color-base.a-text-normal").css("::text").extract()
        product_author = response.css(".a-color-secondary .a-size-base+ .a-size-base").css("::text").extract()
        product_price = response.css(".a-spacing-top-small .a-price:nth-child(1) span").css("::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()

        items['product_name']=product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&lo=list&dc&page='+str(AmazonSpiderSpider.page_number)+'&fst=as%3Aoff&qid=1558349383&rnid=1250225011&ref=sr_pg_1'
        if AmazonSpiderSpider.page_number<=100:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page,callback = self.parse)