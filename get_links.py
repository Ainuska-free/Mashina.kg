import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

URL = 'https://m.mashina.kg/search/all/'
num_pages = input('How many pages to pars YOU WANT')

sub_urls = []
for page in tqdm(range(1, 16)):
  page_url = f'{URL}?page={page}'
  response = requests.get(page_url)
  soup = BeautifulSoup(response.text, 'html.parser')

  for blok_image in soup.find_all('div', class_='list-item list-label'):
    sub_urls.append(f"https://m.mashina.kg{blok_image.find('a')['href']}")

with open('links.json', 'w') as f:
  json.dump(sub_urls, f, indent=4)