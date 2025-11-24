import requests
import csv
from bs4 import BeautifulSoup
import time
import re
import os

def get_page(country):

    wiki_url = "https://en.wikipedia.org/wiki/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )
    } #user agent string to fool wiki page like it's a real user
    
    filename = os.path.join("Laba5.part1\\cache", f"{country}.html")  # "cache/Belarus.html"

    if os.path.exists(filename):
        with open(filename, 'r', encoding="utf-8") as f:
            html = f.read()
    else:
        url = wiki_url + country.replace(" ", "_")
        print(url)

        response = requests.get(url, headers=headers)
        time.sleep(1)
        html = response.text

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(html)

    soup = BeautifulSoup(html, "html.parser")
    return soup



def main():
    countries_source_file = "Laba5.part1/Countries_names.txt"
    countries_info_file = "Laba5.part1/Countries_info.csv"

    #*extract names of countries into list
    with open(countries_source_file, 'r') as countries:
        countries_names = [name.strip() for name in countries.readlines()]

    #* work with countries
    k = 0
    data = [[0] * 4 for _ in range(len(countries_names))]

    for country in countries_names:
        soup = get_page(country)
    ########################################################################################################################
        title = soup.find('title')

        area_th = soup.find('th', string=lambda x: x and "Area" in x)
        area_td = area_th.find_parent('tr').find_next_sibling('tr').find('td')

        population_th = soup.find('th', string=lambda x: x and "Population" in x)
        population = population_th.find_parent('tr').find_next_sibling('tr').find('td')

        capital_th = None
        for th in soup.find_all('th'):
            text = th.get_text(" ", strip=True).lower()
            if "capital" in text:
                capital_th = th
                break
        capital = capital_th.find_next_sibling('td').find('a')

        country = title.text.split(" - ")[0]

        area_text = area_td.get_text(" ", strip=True)
        value_a = re.search(r"[\d,]+", area_text)
        area_value = value_a.group(0).replace(",", "")

        population_text = population.get_text(" ", strip=True)
        value_p = re.search(r"[\d,]+", population_text)
        population_value = value_p.group(0).replace(",", "")

        data[k][0] = country
        data[k][1] = capital.text
        data[k][2] = area_value
        data[k][3] = population_value

        k += 1
    ############################################################################################################

    print(data)
    with open(countries_info_file, 'a', newline="", encoding="utf-8") as countries_info:
        writer = csv.writer(countries_info)
        writer.writerows(data)


main()