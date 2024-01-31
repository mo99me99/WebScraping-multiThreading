import requests
import os.path
from bs4 import BeautifulSoup
import csv

save_dir = './images/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

url = 'https://isorepublic.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


info = []
    
        

def download_images(images, count) : 
    count = count*2
    i = 0
    for image in images: 
        i +=1
        if i%2 ==1 : 
            continue
        try:
            image_url = image.get('src')
            # print(image_url)
            image_data = requests.get(image_url).content
            image_filename = os.path.join(save_dir, image_url.split('/')[-1])
            with open(image_filename, 'wb') as img_file:
                img_file.write(image_data)
            # print(f"Image downloaded: {image_filename}")

        except Exception : 
            continue
        if i > count:
            break
        
        

def fetch_data(images, count):
    count = count*2
    i = 0
    for image in images:
        i +=1
        if i%2 == 1 : 
            continue
        image_info = []
        try:
            image_info.append(image.get('alt'))
            image_info.append(image.get('src'))
            image_info.append(image.get('width'))
            image_info.append(image.get('height'))
            info.append(image_info)
        except Exception:
            continue
        if i > count:
            break
        
        
    # print(info)


with requests.Session() as session:
    response = session.get(url, headers=headers)
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    images = soup.find_all('img')

    # download_images(images,10)
    fetch_data(images,10 )
    # write_info_csv(info)