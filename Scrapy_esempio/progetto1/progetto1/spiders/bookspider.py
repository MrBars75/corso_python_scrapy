import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # Estrai tutti gli articoli con classe 'product_pod'
        books = response.css('article.product_pod')

        for book in books:
            yield{
              'titolo_libro': book.css('h3 a::attr(title)' ).get(),
              'prezzo': book.css('div.product_price p.price_color::text').get()
            }

        next_link = response.css('li.next a::attr(href)').get()

        if next_link is not None:
            if 'catalogue/' in next_link:
                next_page_url = 'https://books.toscrape.com/' + next_link
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_link    
            yield response.follow(next_page_url, callback=self.parse)



