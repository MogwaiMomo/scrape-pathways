# Listing text
response.css("headline h2.profile_header__title::text").get()

# Listing category
response.css("headline h3 a::text").getall()

# Provider (might not be necessary)
response.css("headline h4 a::text").get()

# Contact details (complex text, need to be parsed by BeautifulSoup)
response.css("div.span7half p").getall()

BS: 

from bs4 import BeautifulSoup

def innertext(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text().strip()