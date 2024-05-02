import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["altonsbbqworld.co.uk"]
    start_urls = ["https://altonsbbqworld.co.uk/"]

    def parse(self, response):
        # Define social media domains to look for
        social_media_domains = [
            'facebook.com', 'instagram.com', 'twitter.com',
            'youtube.com', 'linkedin.com', 'tiktok.com'
        ]

        # Extract all the links on the page
        links = response.css('a::attr(href)').getall()
        for href in links:
            if any(domain in href for domain in social_media_domains):
                full_url = response.urljoin(href)
                # Yield the URL if it is a social media link
                yield {
                    'url': full_url
                }

                # Optional: Follow the link (remove the comment)
                # yield scrapy.Request(url=full_url, callback=self.parse_link)

    # You can define this function if you want to do further parsing
    def parse_link(self, response):
        # Process the response of each followed social media link here
        pass
