import craigslist_scraper
from craigslist_scraper import scraper

data = scraper.scrape_url('http://newyork.craigslist.org/mnh/sub/5100979030.html')
print(data.price)


