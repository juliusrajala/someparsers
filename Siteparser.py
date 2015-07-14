# -*- coding: utf-8 -*-
import sys

import requests
from bs4 import BeautifulSoup

from pdfparser import scrapeArticles, downloadFile

def scrapeSite(address):
  page = requests.get(address)
  data = page.content
  soup = BeautifulSoup(data)

  links = soup.find_all('a', class_="issueStyleCoverDate")
  returnables = []
  for link in links:
    print link['href']
    returnables.append("http://online.liebertpub.com/" + link['href'])

  return returnables


def main(argv):
  links = scrapeSite(argv)
  for link in links:
    scrapeArticles(link)


if __name__ == '__main__':
  main(sys.argv[1])
