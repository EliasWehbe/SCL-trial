import os
import sys

os.system('del new.csv')
os.system('scrapy crawl lease -o new.csv -t csv')
os.system('python sendemail.py')

