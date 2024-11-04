import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):

         # Selettore per tutti gli articoli dei libri
        books = response.css('article.product_pod')

        for book in books:
            yield{
                'Titolo' : book.xpath('.//h3/a/@title').get(),
                'Prezzo' : book.xpath('.//p[@class="price_color"]/text()').get(),
                'Rating' : book.xpath('.//p[contains(@class, "star-rating")]/@class').get()
            }
            
        


            
