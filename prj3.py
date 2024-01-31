import requests
import os.path
from bs4 import BeautifulSoup

save_dir = './images/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

url = 'https://isorepublic.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


    
    
        

def download_images(images, count) : 
    i = 0
    count *= 2
    for image in images: 
            try:
                image_url = image.get('src')
                print(image_url)
                image_data = requests.get(image_url).content
                image_filename = os.path.join(save_dir, image_url.split('/')[-1])
                with open(image_filename, 'wb') as img_file:
                    img_file.write(image_data)
                print(f"Image downloaded: {image_filename}")

            except Exception : 
                continue
            finally:
                i +=1
                if i == count:
                    break



with requests.Session() as session:
    response = session.get(url, headers=headers)
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    images = soup.find_all('img')

    download_images(images,10)