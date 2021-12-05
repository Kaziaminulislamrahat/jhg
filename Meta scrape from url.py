import requests
from bs4 import BeautifulSoup

url = 'https://www.ryanscomputers.com/western-digital-120gb-m2-2280-sataiii-ssd-wds120g2g0b'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
metas = soup.find_all('meta')

x=([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'title' ])
y= ([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'keywords' ])
z= ([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ])
print(x,y,z)
#single product meta extract system by python








