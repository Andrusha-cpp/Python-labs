import requests
import csv
from bs4 import BeautifulSoup

countries_source_file = "Countries_names.txt"
countries_info_file = "Countries_info.csv"

countries = open(countries_source_file, 'r')
countries_info = open(countries_info_file, 'w')



countries_info.close()
countries.close()
