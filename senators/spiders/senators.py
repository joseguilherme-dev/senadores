import scrapy
from scrapy.spiders import CrawlSpider
from ..items import SenadoresItem

class SenatorsSpider(CrawlSpider):
    name = 'senators_spider'
    BASE_URL = 'https://www25.senado.leg.br/web/senadores/em-exercicio/-/e/por-nome'
    mongo_collection = 'senators'
    duplicity_condition = ['url']

    def __init__(self):
        pass

    def start_requests(self):
        yield scrapy.Request(url=self.BASE_URL, callback=self.parse_senators_list)

    def parse_senators_list(self, response):
        senators_list = response.xpath('//*[contains(@id,"senadoresemexercicio-tabela-senadores")]/tbody/tr')
    
        for senator in senators_list:
            meta = { 
                'senator_url' : senator.xpath('td[1]/a/@href').extract_first(),
                'senator_name' : senator.xpath('td[1]/a/text()').extract_first(),
                'senator_party' : senator.xpath('td[2]//text()').extract_first(),
                'senator_uf' : senator.xpath('td[3]//text()').extract_first(),
                'senator_period' : senator.xpath('td[4]//text()').extract_first(),
                'senator_phones' : senator.xpath('td[5]//text()').extract_first(),
                'senator_emails' : senator.xpath('td[6]//text()').extract_first()}

            yield scrapy.Request(url=meta.get('senator_url'), meta=meta, callback=self.parse_senator_page)

        return None

    def parse_senator_page(self, response):
        senator = SenadoresItem()
        senator['url'] = response.meta.get('senator_url')
        senator['name']  = response.meta.get('senator_name')
        senator['party'] = response.meta.get('senator_party')
        senator['uf'] = response.meta.get('senator_uf')
        senator['period'] = response.meta.get('senator_period')
        senator['phones'] = response.meta.get('senator_phones')
        senator['email'] = response.meta.get('senator_emails')
        senator['address'] = response.xpath('//div[contains(@class,"dadosPessoais")]/dl/dd[4]//text()').extract_first().strip()
        yield senator
        