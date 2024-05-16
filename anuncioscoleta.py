import scrapy


class AnuncioscoletaSpider(scrapy.Spider):
    name = "base_coleta"
    allowed_domains = ["www.baseimobiliarias.com.br"]
    start_urls = ["https://www.baseimobiliarias.com.br/"]

    def parse(self, response):
        return scrapy.FormRequest.from_response (
            response,
            textboxid = 'finalidade-input'
        )
