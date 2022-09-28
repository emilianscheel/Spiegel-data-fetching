import os
from tkinter import W
from bs4 import BeautifulSoup
import json

dataFolder = os.path.abspath('') + "/data/"
secondDataFolder = os.path.abspath('') + "/data-2/"

htmlKeys = {
    'subtitle': {
        'element': 'span',
        'class': 'block text-primary-base dark:text-dm-primary-base font-sansUI font-bold lg:text-l md:text-l sm:text-base lg:mb-4 md:mb-6 sm:mb-6'
    },
    'title': {
        'element': 'span',
        'class': 'font-brandUI font-extrabold lg:text-7xl md:text-5xl sm:text-4xl leading-tight'
    },
    'shortText': {
        'element': 'div',
        'class': 'RichText RichText--sans leading-loose lg:text-xl md:text-xl sm:text-l lg:mb-32 md:mb-32 sm:mb-24'
    },
    'date': {
        'element': 'div',
        'class': 'font-sansUI lg:text-base md:text-base sm:text-s text-shade-dark dark:text-shade-light'
    },
    'source': {
        'element': 'div',
        'class': 'font-sansUI lg:text-base md:text-base sm:text-s text-shade-dark dark:text-shade-light mt-8'
    },
}


def convert():

    database = []

    filenames = os.listdir(dataFolder)

    for i in range(len(filenames)):

        filename = filenames[i]

        if i == 10:
            break

        f = os.path.join(dataFolder, filename)
        # checking if it is a file
        if os.path.isfile(f):
            html = open(f, encoding='utf-8',
                        errors='ignore').read()

            entry = {
                'title': '',
                'subtitle': '',
                'shortText': '',
                'date': '',
                'source': ''
            }

            soup = BeautifulSoup(html, features="html.parser")

            for key in entry:
                htmlElements = soup.findAll(htmlKeys[key]['element'], {
                    'class': htmlKeys[key]['class']})

                for htmlElement in htmlElements:
                    entry[key] += htmlElement.text.rstrip('\n')

            database.append(entry)

    file = open(secondDataFolder + "database.json", "w")
    file.write(json.dumps(database, ensure_ascii=False, indent=4))
    file.close()


def createDatabaseDir():
    if not os.path.exists(secondDataFolder):
        os.mkdir(secondDataFolder)

    if not os.path.isfile(secondDataFolder + "database.json"):
        open(secondDataFolder + "database.json", "x")
        file = open(secondDataFolder + "database.json",
                    "w")
        file.write(json.dumps([], ensure_ascii=False, indent=4))
        file.close()


if __name__ == "__main__":
    createDatabaseDir()
    convert()
