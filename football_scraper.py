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

            # TAKE THE MINUTE
            minute_pattern = r'[n]\"\>([A-z0-9]{1,2})'
            minute_token = re.search(minute_pattern, str(game))
            minute = minute_token.group(1)

            # FIND THE TEAMS
            teams_pattern = r'[e]\=\"(.{1,40})\"\>'
            teams_token = re.findall(teams_pattern, str(game))
            home_team, away_team = teams_token[0], teams_token[1]

            # FIND THE SCORE
            home_score_pattern = r'[e]\"\>(\d{1,2})\<'
            away_score_pattern = r'[y]\"\>(\d{1,2})\<'
            home_score_token = re.search(home_score_pattern, str(game))
            away_score_token = re.search(away_score_pattern, str(game))
            home_score = home_score_token.group(1)
            away_score = away_score_token.group(1)


scraper = FootballScraper()
scraper.scrape()