'''
Created on Dec 13, 2018

@author: Hiroshige
'''

from googlesearch import search
import csv
import time

keywords = ["レセプト クラウド"]

for keyword in keywords:
        print(keyword)
        for url in search(keyword, stop=50):
            print(url)
        time.sleep(10)

