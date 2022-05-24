#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:46:16 2022

@author: krishshroff
"""
url1 = ""
url2 = ""
url3 = ""
url4 = ""
from selectorlib import Extractor
import requests 
#import csv

# Creating an Extractor by reading from the YAML file

def BookingsScrape(url1):  
    e1 = Extractor.from_yaml_file('BookingsScrape.yml')
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

   # print("Downloading %s"%url)
    r = requests.get(url1, headers=headers) 
    return e1.extract(r.text,base_url=url1)
    #print("---------------")
url1 = str(input("Please input your URL"))
d1 = BookingsScrape(url1)
out = []
out = list(d1.values())
to_csv = out.pop(0)
print(to_csv)
print("---------------")
def GoibiboScrape(url2):
    e2 = Extractor.from_yaml_file('GoibiboScrape.yml')
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

    # print("Downloading %s"%url)
    r = requests.get(url2, headers=headers) 
    return e2.extract(r.text,base_url=url2)
    #print("---------------")
url2 = str(input("Please input your URL"))
d2 = GoibiboScrape(url1)
out = []
out = list(d2.values())
to_csv2 = out.pop(0)
print(to_csv2)
# def MakeMYScrape(url3):
#     e3 = Extractor.from_yaml_file('BookingsScrape.yml')
#     headers = {
#         'Connection': 'keep-alive',
#         'Pragma': 'no-cache',
#         'Cache-Control': 'no-cache',
#         'DNT': '1',
#         'Upgrade-Insecure-Requests': '1',
#         # User Agent - Could be blocked---
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

#         'Referer': 'https://www.booking.com/index.en-gb.html',
#         'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     }

#     # print("Downloading %s"%url)
#     r = requests.get(url3, headers=headers) 
#     return e3.extract(r.text,base_url=url3)
#     #print("---------------")
# def TrivagoScrape(url4):
#     e4 = Extractor.from_yaml_file('BookingsScrape.yml')
#     headers = {
#         'Connection': 'keep-alive',
#         'Pragma': 'no-cache',
#         'Cache-Control': 'no-cache',
#         'DNT': '1',
#         'Upgrade-Insecure-Requests': '1',
#         # User Agent - Could be blocked---
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

#         'Referer': 'https://www.booking.com/index.en-gb.html',
#         'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     }

#     # print("Downloading %s"%url)
#     r = requests.get(url4, headers=headers) 
#     return e4.extract(r.text,base_url=url4)
#     #print("---------------")