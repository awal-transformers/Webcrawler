import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["www.uslgh.com"]
    start_urls = ["https://uslgh.com"]

    def parse(self, response):

        for href in response.css('a::attr(href)').getall():
            yield {
                'url': response.urljoin(href)
            }
        pass
