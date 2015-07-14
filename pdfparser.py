# -*- coding: utf-8 -*-
import sys
import urllib2
import requests
import os
from bs4 import BeautifulSoup

def scrapeArticles(address):
    print address
    page = requests.get(address)
    data = page.content
    soup = BeautifulSoup(data, "html.parser")

    articles = soup.find_all('table', class_="articleEntryTable")
    print len(articles)
    keys = []
    values = []
    for article in articles:
        keys.append(article.find_all('span', class_="hlFld-Title")[0].find_all(text=True)[0])
        values.append(article.find_all('a', class_="pdfLink")[0]['href'])

    data_sets = dict(zip(keys, values))

    print data_sets
    for key in data_sets:
        downloadFile(data_sets[key], key)



def downloadFile(data_set, key):
    pdf_name = key+".pdf"
    for x in range (len(pdf_name)):
        pdf_name=pdf_name.split(" ")
        pdf_name="_".join(pdf_name)
        pdf_name=pdf_name.split("?")
        pdf_name="".join(pdf_name)
        pdf_name=pdf_name.split(":")
        pdf_name="".join(pdf_name)

    if os.path.exists("C:\Users\jijraj\Python\Scripts"+"/" + pdf_name):
        print "Already exists"
        return

    pdf_url = "http://online.liebertpub.com"+data_set
    print pdf_url
    f = requests.get(pdf_url)
    # print pdf_name + " " + str(len(f.content))
    loc_file = open(pdf_name, "wb")
    loc_file.write(f.content)
    loc_file.close()
    print "Completed."


def main(argv):
    scrapeArticles(argv)

if __name__ == '__main__':
    main(sys.argv[1])
