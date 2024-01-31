import requests
from bs4 import BeautifulSoup

url = 'https://isorepublic.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

with requests.Session() as session:
    response = session.get(url, headers=headers)
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.select('.photo-grid-item')

    print(images)
