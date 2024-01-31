import requests
from bs4 import BeautifulSoup

response = requests.get('https://stackoverflow.com/questions')

soup = BeautifulSoup(response.text, 'html.parser')

questions = soup.select('.s-post-summary')

# print(questions[0].get('id'))

# print(questions[0].select('.s-post-summary--content-title'))

# print(questions[0].select_one('.s-post-summary--content-title').getText())

for question in questions:
    print(question.select_one('.s-post-summary--content-title').getText())
    print(question.select_one('.s-post-summary--stats-item').select_one('.s-post-summary--stats-item-number').getText())