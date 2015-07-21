__author__ = 'eliaswehbe'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from random import randint

driver = webdriver.Firefox()

driver.get('https://newyork.craigslist.org/search/sub')

elem = driver.find_element_by_id('query')  # Find the search box
elem.send_keys('lease' + Keys.RETURN)

listings = driver.find_elements_by_class_name("hdrlnk")
listings_link_list = []

for i in range (0, len(listings)):
        listings_link_list.append(listings[i].get_attribute("href"))

print(listings_link_list)
print(listings_link_list[1])

listings_dict = { "url":"","title":"","price":"","body":"","bedrooms":"","posting_id":"","posting_time":"","posting_update": ""}


for i in range(0,25,1):
    sleep(randint(1,15))
    driver.get(str(listings_link_list[i]))
    listings_dict["url"] = ""
    listings_dict["title"] = driver.find_element_by_class_name("postingtitletext").text
    listings_dict["price"] = driver.find_element_by_class_name("price").text
    listings_dict["body"] = driver.find_element_by_id("postingbody").text
    listings_dict["bedrooms"] = driver.find_element_by_class_name("attrgroup").text
    listings_dict["posting_id"] = driver.find_element_by_class_name("postinginfo").text
    posting_times = driver.find_elements_by_tag_name("time")
    listings_dict["posting_time"] = posting_times[1].get_attribute("datetime")
    try:
        posting_update = posting_times[2].get_attribute("datetime")
        listings_dict["posting_update"] = posting_update
    except:
        listings_dict["posting_update"] = ""
        pass
    driver.back()

print(listings_dict)





    








