from dataclasses import dataclass, field
import requests
import json


#zoo animals            https://zoo-animal-api.herokuapp.com/
@dataclass
class Animal:
    name: str
    latin_name: str
    animal_type: str
    active_time: str
    length_min: float
    length_max: float
    weight_min: float
    weight_max: float
    lifespan: int
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id: int


#Anime Facts         https://chandan-02.github.io/anime-facts-rest-api/   
@dataclass
class Anime:
    anime_id: int
    anime_name: str
    anime_img: str


@dataclass
class AnimeFacts:
    fact_id: int
    fact: str


#Studio Ghibili         https://ghibliapi.herokuapp.com/

@dataclass
class StudioGhibli:
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


#Colors             https://x-colors.herokuapp.com/
@dataclass
class color:
    hex: str
    rgb: str
    hsl: str




#zoo animals
response =requests.get('https://zoo-animal-api.herokuapp.com/animals/rand/5')       #5 for 5 instances
#dir(response)
responseDict = response.json()
#print(type(responseDict))
classList = [{},{},{},{},{}]
#print(classList)


#for num in range(0,5):
 #   classList[num]=Animal(responseDict[num]['name'],responseDict[num]['latin_name'],responseDict[num]['animal_type'],responseDict[num]['active_time'],responseDict[num]['length_min'],responseDict[num]['length_max'],responseDict[num]['weight_min'],responseDict[num]['weight_max'],responseDict[num]['lifespan'],responseDict[num]['habitat'],responseDict[num]['diet'],responseDict[num]['geo_range'],responseDict[num]['image_link'],responseDict[num]['id'])
    
#for animal in classList:
 #   print(animal)
    



#Anime
response =requests.get('https://anime-facts-rest-api.herokuapp.com/api/v1')       #5 for 5 instances
responseDict = response.json()
responseDict=responseDict['data']
print(type(responseDict))
classList = []


for num in range(0,5):
    classList.append(Anime(responseDict[num]['anime_id'],responseDict[num]['anime_name'],responseDict[num]['anime_img']))
    
print(classList[0])
for anime in responseDict:
    print(anime)



#Studio Ghibli
response =requests.get('https://ghibliapi.herokuapp.com/films')
responseDict = response.json()
print(type(responseDict))
classList = []

for num in range(0,5):
    classList.append(StudioGhibli(responseDict[num]['id'],responseDict[num]['title'],responseDict[num]['original_title'],responseDict[num]['original_title_romanised'],responseDict[num]['description'],responseDict[num]['director'],responseDict[num]['producer'],responseDict[num]['release_date'],responseDict[num]['running_time'],responseDict[num]['rt_score'],responseDict[num]['url']))
    
for movie in responseDict:
    print(movie)





