import requests

from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Please insert rating:"))


headers = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class","ratingColumn imdbRating"})




for header, rating in zip(headers,ratings):
    header = header.text
    rating = rating.text

    header = header.strip()
    header = header.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > a):
        print("Movie name: {} Movie Rating : {}".format(header,rating))