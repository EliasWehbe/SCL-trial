# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ContactItem(Item):
    Email = Field()
    Phone = Field()
    LinkAddress = Field()

class LeaseItem(Item):
    url = Field()
    title = Field()
    price = Field()
    body = Field()
    bedrooms = Field()
    posting_id = Field()
    posting_time = Field()
    posting_update = Field()
    scrape_date = Field()
    email = Field()
    email_date = Field()
