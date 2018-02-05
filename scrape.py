import xml.etree.ElementTree as ET

file = "videodb.xml" # the exported kodi library xml file

# parse the xml file and get the root
tree = ET.parse(file)
root = tree.getroot() 

# open the movie list output file
with open('movies.txt', 'w') as output:
    # output the header row
    output.write('Title\tGenre\tYear\tStudio\n')
    # for movie tag find the title genre year and studio then write the row to the file
    for movie in root.findall('movie'):
        movieInfo = {}
        movieInfo['title'] = movie.find('title').text
        movieInfo['genre'] = [item.text for item in movie.findall('genre')]
        movieInfo['year'] = movie.find('year').text
        # try block needed in case there is not a studio tag
        try:
            movieInfo['studio'] = movie.find('studio').text
        except:
            movieInfo['studio'] = ' '
        output.write('{}\t{}\t{}\t{}\n'.format(movieInfo['title'], movieInfo['genre'], movieInfo['year'], movieInfo['studio']))

# open the tv list output file
with open('tv.txt', 'w') as output:
    # output the header row
    output.write('Title\tGenre\tYear\tStudio\n')
    # for tv show tag find the title genre year and studio then write the row to the file
    for show in root.findall('tvshow'):
        showInfo = {}
        showInfo['title'] = show.find('title').text
        showInfo['genre'] = [item.text for item in show.findall('genre')]
        showInfo['year'] = show.find('year').text
        # try block needed in case there is not a studio tag
        try:
            showInfo['studio'] = show.find('studio').text
        except:
            showInfo['studio'] = ' '
        output.write('{}\t{}\t{}\t{}\n'.format(showInfo['title'], showInfo['genre'], showInfo['year'], showInfo['studio']))

with open('disney.txt', 'w') as output:
    # output the header row
    output.write('Title\tGenre\tYear\tStudio\n')
    # create dictionary with all disney movies titles as keys and the associated year as the value
    with open('disneyList.txt', 'r') as inFile:
        inFile.readline()
        disneyList = {}
        for line in inFile:
            line = line.strip()
            values = line.split('\t')
            disneyList[values[0]] = values[1]
    # for tv show tag find the title genre year and studio then write the row to the file    
    for movie in root.findall('movie'):
        disneyInfo = {}
        disneyInfo['title'] = movie.find('title').text
        disneyInfo['genre'] = [item.text for item in movie.findall('genre')]
        disneyInfo['year'] = movie.find('year').text
        try:
            disneyInfo['studio'] = movie.find('studio').text
        except:
            disneyInfo['studio'] = ' '
        if disneyInfo['title'] in list(disneyList.keys()) and disneyInfo['year'] == disneyList[disneyInfo['title']]:
            output.write('{}\t{}\t{}\t{}\n'.format(disneyInfo['title'], disneyInfo['genre'], disneyInfo['year'], disneyInfo['studio']))