# Structure:

# <section data-section="{name of section}"> 

# <h2 class="SectionTitle_sectionTitle__WTUrW SectionTItleSpotlight_yellow__Z2L9j SectionTitleVariant_standard__bBxha SectionTItleTheme_borderStandard__6qpJH" title="[NAME OF HEADER]"> 
# <span class="SectionTitle_titleText__bXKXt SectionTitle_imageOnRight__Vqw1P"> {HEADERS as text} </span>
# </h2>

# <article> {Article under header} 
# <a href="{link}">
# <h3 class="[...]"> {TITLE OF ARTICLE} </h3>
# </a>
# </article>

# </section>

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://www.onet.pl"

data = requests.get(url).text
soup = BeautifulSoup(data, "html.pars.er")

date = pd.to_datetime('today').strftime('%Y-%m-%d')

headers = ['section_title', 'article_title', 'date']
df = pd.DataFrame(columns=headers)


for section in soup.find_all('section'):
    
    try:
        section_title = section.find_all('h2')[0].get('title')
    except IndexError:
       section_title = 'None'
    

    for article in section.find_all('article'):
        article_title = article.get_text()
        
        new_row = pd.Series(data=[section_title, article_title, date], index=headers)

        df = df._append(new_row, ignore_index = True)


path = os.getcwd() + '\\article_list\\' + date +'.txt'
df.to_csv(path_or_buf=path ,index=False)