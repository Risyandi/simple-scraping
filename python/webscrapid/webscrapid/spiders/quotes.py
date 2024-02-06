import scrapy

class QuotesSpider(scrapy.Spider):
    # define the urls to crawl
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/inspirational/" ]

    #  handle the response from each url
    def parse(self, response):
        # get data crawl
        for quote in response.css("div.quote"):
            yield {
                "quotesAuthor":  quote.xpath("span/small/text()").get(),
                "quotesText": quote.css("span.text::text").get(),
                } 
                
        #  follow pagination links
        next_page = response.css('li.next a::attr("href")').get()
        
        # handle next_page is not none
        if  next_page is not None:
            yield response.follow(next_page, self.parse)
