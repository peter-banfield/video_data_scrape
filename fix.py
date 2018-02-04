import re

numPat = re.compile('\d+\.')
ratePat = re.compile('\([\w-]+\)')
yearPat = re.compile('\d\d\d\d')
studioPat = re.compile('\([\w ]+\)')

with open('list of disney movies.txt', 'r') as inFile:
    with open('disneyList.txt', 'w') as outFile:
        outFile.write('Title\tYear\n')
        for line in inFile:
            numMatch = numPat.search(line).span()
            yearMatch = yearPat.search(line).span()
            try:
                rateMatch = ratePat.search(line).span()
                rate = line[rateMatch[0]:rateMatch[1]].strip()
                rawTitle = line[yearMatch[1]:rateMatch[0]].strip()
            except:
                rawTitle = line[yearMatch[1]:].strip()
                rate = ' '
            studioMatch = studioPat.search(rawTitle)
            if studioMatch:
                studio = rawTitle[studioMatch.span()[0]:studioMatch.span()[1]].strip()
                title = rawTitle[:studioMatch.span()[0]]
            else:
                studio = ' '
                title = rawTitle

            num = line[numMatch[0]:numMatch[1]].strip()
            year = line[yearMatch[0]:yearMatch[1]].strip()
            

            outFile.write('{}\t{}\n'.format(title, year))
