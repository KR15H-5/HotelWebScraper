from curses import KEY_SCOMMAND
from selectorlib import Extractor
import requests
import csv


e = Extractor.from_yaml_file("/Users/krishshroff/Desktop/KRISH/Programming/booking-hotel-scraper/BookingsScrapee.yml")


def scrape(url):    
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        # User Agent - Could be blocked---
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        'Referer': 'https://www.booking.com/index.en-gb.html',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    print("Downloading %s"%url)
    r = requests.get(url, headers=headers) 
    return e.extract(r.text,base_url=url)
    print("---------------")

# product_data = []
url = str(input("Please input your URL"))
d1 = scrape(url)
#print(d1)
out = list(d1.values())
to_csv = out.pop(0)
print(to_csv)

#keys = to_csv[0].keys()
with open('HotelData.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, to_csv) #keys originally
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)