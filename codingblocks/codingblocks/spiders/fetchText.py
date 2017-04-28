import scrapy


class start(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['codingblocks.net']
    start_urls = ['http://www.codingblocks.net/episode1']
    curPage = 1
    content = []

    def parse(self, response):
        self.content += ''.join(response.css('article.post').extract())
        self.curPage += 1
        if self.curPage is 45:
            with open('./all.html', 'w') as file:
                file.write(''.join(self.content))
            return

        print(self.start_urls[0][:-1] + str(self.curPage))
        yield scrapy.Request(self.start_urls[0][:-1] + str(self.curPage), callback=self.parse)
