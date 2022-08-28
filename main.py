import application
import datetime 
from bs4 import BeautifulSoup as BS
import requests
from pprint import pprint



url = 'https://stopgame.ru/games/PC/best?year_start=2021&year_end=2021'
request = requests.get(url)
soup = BS(request.text, 'html.parser')
game_names = soup.find_all('div', class_= 'caption caption-bold')
for name in game_names:
    g_name = name.text.strip()
    print(g_name)
    
if __name__ == '__main__':
    date_now = datetime.date.today()
    print(date_now)
    application.calculate_salary()
    application.get_employees()
    print(dir(application))
