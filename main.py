#!/usr/bin/python3

import urllib3
from datetime import datetime
import json
import os
import feedparser


dataFolder = os.path.abspath('') + "/data/"


def createDatabaseDir():
    if not os.path.exists(dataFolder):
        os.mkdir(dataFolder)


def fetch():

    NewsFeed = feedparser.parse(
        "https://www.spiegel.de/schlagzeilen/index.rss")

    for entry in NewsFeed.entries:
        http = urllib3.PoolManager()
        request = http.request('GET', entry['link'])
        if (request.status != 200):
            return
        html = request.data.decode('utf-8')

        # save html

        filename = (entry['id']
                    .replace('https://www.spiegel.de', '')
                    .replace('/', '-')
                    .replace('-', '', 1) + ".html")

        if not os.path.isfile(dataFolder + filename):
            open(dataFolder + filename, "x")

        file = open(dataFolder + filename, "w")
        file.write(html)
        file.close()


if __name__ == "__main__":
    createDatabaseDir()
    fetch()
