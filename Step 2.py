# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# data_mapping = {
#     'Country': ('h1', {'class': 'firstHeading'}),
#     'GDP': ('th', {'string': 'GDP'}),
#     'Capital': ('th', {'string': 'Capital'}),
#     'Native Languages': ('th', {'string': 'Official languages'}),
#     'Area': ('th', {'string': 'Area'}),
#     'Population': ('th', {'string': 'Population'}),
# }

# def extract_text_by_header(table, header):
#     row = table.find('th', string=header)
#     if row:
#         data = row.find_next('td')
#         if data:
#             return data.get_text(strip=True)
#     return None

# def scrape_country_data(url):
#     response = requests.get(url)

#     if response.status_code == 200:
#         html_content = response.text
#         soup = BeautifulSoup(html_content, 'html.parser')

#         country_data = {}
#         for key, tag_info in data_mapping.items():
#             if key == 'Country':
#                 tag_type, tag_value = tag_info
#                 tag_content = soup.find(tag_type, tag_value)
#                 if tag_content:
#                     country_data[key] = tag_content.get_text(strip=True)
#             else:
#                 country_data[key] = extract_text_by_header(soup.find('table', {'class': 'infobox'}), tag_info[1]['string'])

#         return country_data
#     else:
#         print(f"Unable to find content in {url}. Error code {response.status_code}")
#         return None

# urls = [
#     'https://en.wikipedia.org/wiki/Canada',
#     'https://en.wikipedia.org/wiki/United_States',
#     'https://en.wikipedia.org/wiki/United_Kingdom',
#     'https://en.wikipedia.org/wiki/Korea',
#     'https://en.wikipedia.org/wiki/France',
#     'https://en.wikipedia.org/wiki/Turkey',
#     'https://en.wikipedia.org/wiki/Italy'
# ]

# country_data = []

# for url in urls:
#     data = scrape_country_data(url)
#     if data:
#         country_data.append(data)

# hcd = pd.DataFrame(country_data)

# # saving it to a CSV file
# hcd.to_csv('country_data.csv', index=False)

# print(hcd)

import requests
from bs4 import BeautifulSoup
import pandas as pd

data_mapping = {
    'Country': ('h1', {'class': 'firstHeading'}),
    'GDP': ('table tr:nth-of-type(34) td:nth-of-type(1) span:nth-of-type(2)', None),
    'Capital': ('table tr:nth-of-type(6) td a', None),
    'Native Languages': ('th', {'string': 'Official languages'}),
    'Area': ('table tr:nth-of-type(26) td', None),
    'Population': ('table tr:nth-of-type(30) td', None),
}

def extract_text_by_xpath(soup, xpath):
    element = soup.select_one(xpath)
    if element:
        return element.get_text(strip=True)
    return None

def scrape_country_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        country_data = {}
        for key, (selector, _) in data_mapping.items():
            if key == 'Country':
                tag_type, tag_value = selector
                tag_content = soup.find(tag_type, tag_value)
                if tag_content:
                    country_data[key] = tag_content.get_text(strip=True)
            else:
                if key == "GDP":
                    country_data[key] = extract_text_by_xpath(soup, selector)
                    if not country_data[key]: country_data[key] = extract_text_by_xpath(soup, 'table tr:nth-of-type(40) td') 
                else: country_data[key] = extract_text_by_xpath(soup, selector)

        return country_data
    else:
        print(f"Unable to find content in {url}. Error code {response.status_code}")
        return None

urls = [
    'https://en.wikipedia.org/wiki/Canada',
    'https://en.wikipedia.org/wiki/United_States',
    'https://en.wikipedia.org/wiki/United_Kingdom',
    'https://en.wikipedia.org/wiki/Korea',
    'https://en.wikipedia.org/wiki/France',
    'https://en.wikipedia.org/wiki/Turkey',
    'https://en.wikipedia.org/wiki/Italy'
]

country_data = []

for url in urls:
    data = scrape_country_data(url)
    if data:
        country_data.append(data)

hcd = pd.DataFrame(country_data)

# saving it to a CSV file
hcd.to_csv('country_data.csv', index=False)

print(hcd)
