import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=Engineer&geo%5Bc%5D%5B0%5D=1']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacansy = response.xpath("//a[contains(@class, 'icMQ_ _1QIBo')]/@href'")

        for link in vacansy:
            yield response.follow(link, callback=self.vacansy_parse)


    def vacansy_parse(self, response: HtmlResponse):
        link_vac = response.url
        name = response.xpath("//h1[@class='_3mfro rFbjy s1nFK _2JVkc']/text()")
        print(name)
        if response.xpath("//span[@class='_3mfro _2Wp8I ZON4b PlM3e _2JVkc']/text()"):
            salary = response.xpath("//span[@class='_3mfro _2Wp8I ZON4b PlM3e _2JVkc']/text()")
        else:
            salary=''
        link = 'superjob.ru'
        # print(name, salary)
        yield JobparserItem(name=name, salary_from=''.join(salary), salary_to='', link_vac=link_vac, link_site=link)


