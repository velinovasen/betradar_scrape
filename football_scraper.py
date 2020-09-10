from bs4 import BeautifulSoup
from selenium.webdriver import FirefoxOptions, Firefox
import re
import sqlite3
from time import sleep


class FootballScraper:
    WEB_LINKS = {
        "football": "https://cs.betradar.com/sportcenter/soccer"
    }

    def scrape(self):

        # CONNECT THE DATABASE
        connector = sqlite3.connect('games.db')
        cursor = connector.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS allGames('
                       ' minute TEXT, home_team TEXT, away_team TEXT,'
                       ' home_score DECIMAL, away_score DECIMAL,'
                       ' home_odd REAL, draw_odd REAL, away_odd REAL)')

        options = FirefoxOptions()
        options.headless = True
        driver = Firefox(options=options, executable_path='C:\Windows\geckodriver.exe')
        driver.get(self.WEB_LINKS["football"])
        sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/i').click()
        sleep(1)
        html = driver.execute_script('return document.documentElement.outerHTML;')

        soup = BeautifulSoup(html, 'html.parser')
        games = soup.find_all(class_=re.compile("sr-match-container sr-border"))
        all_games = [game for game in games]
        driver.close()

        for game in all_games:
            print(str(game))
            minute_pattern = r'[n]\"\>([A-z0-9]{1,2})'
            minute = re.search(minute_pattern, str(game))
            print(type(minute))
            print(minute)


scraper = FootballScraper()
scraper.scrape()