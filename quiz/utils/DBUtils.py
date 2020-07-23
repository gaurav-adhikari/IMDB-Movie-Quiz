""" Database Utilities """

import re
import requests
from bs4 import BeautifulSoup

from quiz import db
from quiz.Models import UserInfo

from quiz.utils.Utils import generatePasswordHash


def adminEntryCheckHelper():
    "Checks if the user 'admin' is added to the DB , if not Adds admin to the DB"

    if UserInfo.query.filter_by(username="admin").first() == None:
        adminUser = UserInfo(username="admin", password=generatePasswordHash(
            "admin"), email="admin@admin.com", referralCode="admin")
        try:
            db.session.add(adminUser)
            db.session.commit()
        except:
            db.rollback()


def getIMDBQuestions():
        
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    imdb = []

    for index in range(0, len(movies)):

        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index))-(len(movie))]
        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "vote": votes[index],
                "link": links[index]}
        imdb.append(data)

    for item in imdb:
        print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])