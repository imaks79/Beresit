from bs4 import BeautifulSoup

import requests
import pandas as pd

# URL = 'https://meteo-dv.ru/hydro_dfo/cgi/geospace_wolf.php?'
URL = 'https://meteo-dv.ru/geospace/averageMonthW'; 
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}; 


def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params); 
    return r;   


def parse():
    html = get_html(URL); 
    if html.status_code == 200:
        get_content(html.text); 
    else:
        print('ERROR'); 


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser'); 
    # ---------- # __________ # ---------- #
    months = []; 
    coef = []; 
    pos = []; 
    years = []; 
    tab_1 = {}; 
    res = {}; 
    # ---------- # __________ # ---------- #
    items_1 = soup.find_all('th', class_ = None); 
    for i in range(3, len(items_1)):
      months.append(items_1[i].text); 
    items_2 = soup.find_all('td', class_ = 'edit'); 
    i = 0; 
    for item in items_2:
      years.append(item.get('data-year')); 
      pos.append(int(item.get('data-pos'))); 
      coef.append(item.text); 
    while years[i] == years[0] and i < 12:
      tab_1[months[i]] = coef[i]; 
      i += 1; 
    res[years[0]] = tab_1; 
    df = pd.DataFrame(res); 
    df.to_csv('coefficient.csv', header = True, index = True); 