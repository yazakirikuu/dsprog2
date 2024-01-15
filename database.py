import requests
from bs4 import BeautifulSoup
import pandas as pd

regions = ['Oceania', 'Asia', 'Africa', 'Europe']

data_list = []

for region in regions:
    url = f"https://gs.statcounter.com/os-market-share/desktop/{region}"

    # ウェブサイトからHTMLを取得
    response = requests.get(url)
    html = response.text

    # BeautifulSoupでHTMLをパース
    soup = BeautifulSoup(html, 'html.parser')

    # プラットフォームの情報を取得
    rows = soup.find_all('tr', class_='col col-span-2')
    
    platforms = []

    for row in rows:
        platform = row.find('th').get_text(strip=True)
        share_span = row.find('span', class_='count')
        share = share_span.get_text(strip=True) if share_span else "N/A"
        share_percentage = float(share.replace('%', '')) if share != "N/A" else None
        platforms.append({'Region': region, 'Platform': platform, 'Share': share_percentage})