import requests
import csv
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0 Safari/537.36"
    )
} #user agent string to fool wiki page like it's a real user

url = "https://en.wikipedia.org/wiki/Belarus"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
time.sleep(1)

title = soup.find('title')
print(title.text)
time.sleep(1)

area_th = soup.find("th", string=lambda x: x and "Area" in x)
time.sleep(1)
area_td = area_th.find_parent('tr').find_next_sibling('tr').find('td')
print(area_td.text)
time.sleep(1)

population_th = soup.find("th", string=lambda x: x and "Population" in x)
time.sleep(1)
population = population_th.find_parent('tr').find_next_sibling('tr').find('td')
print(population.text)
time.sleep(1)

capital_th = None
for th in soup.find_all("th"):
    text = th.get_text(" ", strip=True).lower()
    if "capital" in text:
        capital_th = th
        break
time.sleep(1)
capital = capital_th.find_next_sibling('td').find('a')
print(capital.text)
time.sleep(1)



url = "https://en.wikipedia.org/wiki/Germany"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
time.sleep(1)

title = soup.find('title')
print(title.text)
time.sleep(1)

area_th = soup.find("th", string=lambda x: x and "Area" in x)
time.sleep(1)
area_td = area_th.find_parent('tr').find_next_sibling('tr').find('td')
print(area_td.text)
time.sleep(1)

population_th = soup.find("th", string=lambda x: x and "Population" in x)
time.sleep(1)
population = population_th.find_parent('tr').find_next_sibling('tr').find('td')
print(population.text)
time.sleep(1)

capital_th = None
for th in soup.find_all("th"):
    text = th.get_text(" ", strip=True).lower()
    if "capital" in text:
        capital_th = th
        break
time.sleep(1)
capital = capital_th.find_next_sibling('td').find('a')
print(capital.text)
time.sleep(1)