import pandas as pd
import re

country_data = [
    {'Country': 'Canada', 'GDP': '$2.379 trillion', 'Capital': 'Ottawa', 'Native Languages': 'English and French', 'Area': '9,984,670 km2', 'Population': '40,097,761'},
    {'Country': 'United States', 'GDP': '$26.950 trillion', 'Capital': 'Washington, D.C.', 'Native Languages': 'English', 'Area': '3,796,742 sq mi', 'Population': '333,287,557'},
    {'Country': 'United Kingdom', 'GDP': '$3.872 trillion', 'Capital': 'London', 'Native Languages': 'English', 'Area': '242,495 km2', 'Population': '66,971,411'},
    {'Country': 'Korea', 'GDP': '$1.721 trillion', 'Capital': 'Seoul', 'Native Languages': 'Korean', 'Area': '100,210 km2', 'Population': '51,784,059'}
]

hcd = pd.DataFrame(country_data)
    # highest country data variable created

hcd['GDP'] = hcd['GDP'].apply(lambda x: float(re.findall("[$\d.]+", x)[0].replace("$", '')))
hcd['Area'] = hcd['Area'].replace('[^\d.]', '', regex=True).astype(float)
hcd['Population'] = hcd['Population'].replace('[^\d.]', '', regex=True).astype(float)

highest_population = hcd.loc[hcd['Population'].idxmax()]['Country']
highest_area = hcd.loc[hcd['Area'].idxmax()]['Country']
highest_GDP = hcd.loc[hcd['GDP'].idxmax()]['Country']

print(f"Country with the highest population: {highest_population}")
print(f"Country with the highest area: {highest_area}")
print(f"Country with the highest GDP: {highest_GDP}")
