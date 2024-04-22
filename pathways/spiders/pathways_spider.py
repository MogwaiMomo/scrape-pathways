from pathlib import Path

import scrapy

class PathwaysSpider(scrapy.Spider):

    ids_00s = list(range(1, 100)) # current
    ids_100s = list(range(101, 200)) # 1st pass done
    ids_200s = list(range(201, 300)) # 1st pass done
    ids_300s = list(range(301, 400)) # 1st pass done
    ids_400s = list(range(401, 500)) # 1st pass done
    ids_500s = list(range(501, 600)) # 1st pass done
    ids_600s = list(range(601, 700)) # 1st pass done
    ids_700s = list(range(701, 800)) # 1st pass done
    ids_800s = list(range(801, 900)) # 1st pass done
    ids_900s = list(range(901, 996)) # 1st pass done
    
    name = "pathways"
    start_urls = [ "https://victoria-southisland.pathwaysbc.ca/programs/"+str(i) for i in ids_00s]

    def parse(self, response):

        yield {
            "url": response.request.url, # listing URL. Might change!
            "name": response.css("div.headline h2.profile_header__title::text").get(),
            "category": response.css("div.headline h3 a::text").getall(),
            "description": response.css("div.headline div:nth-child(4) i div::text").getall(),
            "contact_html": response.css("div.span7half p").getall()
        }



