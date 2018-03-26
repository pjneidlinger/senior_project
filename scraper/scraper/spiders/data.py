import scrapy


class PointsSpider(scrapy.Spider):
    name = "points"
    start_urls = [
        'https://www.basketball-reference.com/leagues/NBA_2018_leaders.html'
    ]

    def parse(self, response):
        filename = 'points-%s.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {
#                'text': quote.html('<main class="stats-container">').extract_first(),
#            }
