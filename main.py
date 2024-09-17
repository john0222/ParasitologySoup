import requests
from bs4 import BeautifulSoup
import os
import datalogger as dl
# header setup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    #這行抄來的
}

def fetch_image_urls(query, num_images):
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    image_urls = []
    img_tags = soup.find_all('img', {'class': 't0fcAb'})  # google search class 
    
    for img in img_tags:
        if len(image_urls) >= num_images:
            break
        img_url = img.get('src')
        if img_url and img_url.startswith('http'):
            image_urls.append(img_url)
    
    return image_urls

def download_images(image_urls, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for i, img_url in enumerate(image_urls):
        try:
            response = requests.get(img_url, headers=headers)
            with open(os.path.join(folder_path, f'image_{i+1}.jpg'), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded image_{i+1}.jpg")
            dl.log(f"Downloaded image_{i+1}.jpg")
        except Exception as e:
            print(f"Could not download {img_url}. Reason: {e}")
            dl.log(f"Could not download {img_url}. Reason: {e}")


def main():
    dl.create_log()
    keywords = input("Enter keywords for the images (comma-separated): ").split(',')
    num_images = int(input("Enter the number of images to download per keyword: "))
    
    for keyword in keywords:
        keyword = keyword.strip()
        print(f"Fetching images for: {keyword}")
        dl.log(f"Fetching images for: {keyword}")
        image_urls = fetch_image_urls(keyword, num_images)
        if image_urls:
            download_images(image_urls, f'images/{keyword}')
            dl.log(f"Downloaded images for: {keyword}")
        else:
            print(f"No images found for {keyword}")
            dl.log(f"No images found for {keyword}")

if __name__ == "__main__":
    main()
 