import xml.etree.ElementTree as ET
import csv

file = "videodb.xml"

tree = ET.parse(file)

root = tree.getroot()
with open('movies.csv', 'w') as output:
    movieFields = ['title', 'genre', 'year', 'studio']
    writer = csv.DictWriter(output, fieldnames=movieFields)
    writer.writeheader()
    for movie in root.findall('movie'):
        movieInfo = {}
        movieInfo['title'] = movie.find('title').text
        movieInfo['genre'] = [item.text for item in movie.findall('genre')]
        movieInfo['year'] = movie.find('year').text
        try:
            movieInfo['studio'] = movie.find('studio').text
        except:
            movieInfo['studio'] = ' '
        writer.writerow(movieInfo)

with open('tv.csv', 'w') as output:
    tvFields = ['title', 'genre', 'year', 'studio']
    writer = csv.DictWriter(output, fieldnames=tvFields)
    writer.writeheader()
    for show in root.findall('tvshow'):
        showInfo = {}
        showInfo['title'] = show.find('title').text
        showInfo['genre'] = [item.text for item in show.findall('genre')]
        showInfo['year'] = show.find('year').text
        try:
            showInfo['studio'] = show.find('studio').text
        except:
            showInfo['studio'] = ' '
        writer.writerow(showInfo)

with open('disney.csv', 'w') as output:
    movieFields = ['title', 'genre', 'year', 'studio']
    writer = csv.DictWriter(output, fieldnames=movieFields)
    writer.writeheader()
    for movie in root.findall('movie'):
        try:
            if 'disney' in movie.find('studio').text.lower() or 'pixar' in movie.find('studio').text.lower():
                movieInfo = {}
                movieInfo['title'] = movie.find('title').text
                movieInfo['genre'] = [item.text for item in movie.findall('genre')]
                movieInfo['year'] = movie.find('year').text
                try:
                    movieInfo['studio'] = movie.find('studio').text
                except:
                    movieInfo['studio'] = ' '
                writer.writerow(movieInfo)
        except:
            pass