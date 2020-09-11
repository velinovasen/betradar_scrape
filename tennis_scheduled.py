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
        options.headless = False
        driver = Firefox(options=options, executable_path='C:\Windows\geckodriver.exe')
        driver.get(self.WEB_LINKS["tennis"])
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div").click()
        elements = driver.find_elements_by_class_name("sr-tournament sr-collapsed")
        [print(el) for el in elements]
        time.sleep(15)
        html = driver.execute_script('return document.documentElement.outerHTML;')

        soup = BeautifulSoup(html, 'html.parser')
        games = soup.find_all(class_=re.compile("sr-tournament sr-collapsed"))
        [game.click() for game in games] # TO FINISH NOT WORKING !
        driver.close()


scraper = TennisScheduled()
scraper.scrape()
