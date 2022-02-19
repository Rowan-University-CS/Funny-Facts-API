from bs4 import BeautifulSoup
import requests
import json


URLS = [
'https://bestlifeonline.com/funniest-facts/',
'https://bestlifeonline.com/random-facts/'
]


if __name__ == "__main__":
    data = []
    for url in URLS:
        req_content = requests.get(url).content
        soup = BeautifulSoup(req_content, 'html.parser')
        
        header_mods = soup.find_all('h2', attrs={'class': 'header-mod'})
        for div_title in header_mods:
            div_titles = div_title.find_all('div', attrs={'class': 'title'})
            for title in div_titles: 
                item = {'fact': title.text.strip()}
                data.append(item)
    json_string = json.dumps(data, indent=4)
    with open('facts_data.json', 'w') as output:
        output.write(json_string)