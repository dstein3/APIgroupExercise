import requests
import csv
import json
from bs4 import BeautifulSoup
from dataclasses import dataclass, field

#Studio Ghibli

response = requests.get('https://ghibliapi.herokuapp.com/films')

responseDict = response.json()

print(type(responseDict))

classList = []


@dataclass
class AnimeFacts:
    id: str
    title: str
    original_title: str
    original_title_romanised: str
    description: str 
    director: str
    producer: str
    release_date: str
    running_time: str
    rt_score: str
    url: str

for num in range(0,5):
    classList.append(AnimeFacts(responseDict[num]['id'],responseDict[num]['title'],responseDict[num]['original_title'],responseDict[num]['original_title_romanised'],responseDict[num]['description'],responseDict[num]['director'],responseDict[num]['producer'],responseDict[num]['release_date'],responseDict[num]['running_time'],responseDict[num]['rt_score'],responseDict[num]['url']))


print(classList)
# for movie in responseDict:
#     print(movie)