from bs4 import BeautifulSoup
from selenium.webdriver import FirefoxOptions, Firefox
import re
import time
import sqlite3


class TennisScheduled:
    WEB_LINKS = {
        "tennis": 'https://cs.betradar.com/sportcenter/tennis'
    }

    def scrape(self):
        # TO DO - CONNECT THE DATABASE

        # GET THE HTML
        options = FirefoxOptions()
        options.headless = True
        driver = Firefox(options=options, executable_path='C:\Windows\geckodriver.exe')
        driver.get(self.WEB_LINKS["tennis"])
        time.sleep(2)
        html = driver.execute_script('return document.documentElement.outerHTML;')

        soup = BeautifulSoup(html, 'html.parser')
        games = soup.find_all(class_=re.compile("sr-tournament sr-collapsed"))
        [print(game) for game in games]
        driver.close()


scraper = TennisScheduled()
scraper.scrape()
