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
        options = FirefoxOptions()
        options.headless = False
        driver = Firefox(options=options, executable_path='C:\Windows\geckodriver.exe')
        driver.get(self.WEB_LINKS["football"])
        sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/i').click()
        sleep(1)
        html = driver.execute_script('return document.documentElement.outerHTML;')

        soup = BeautifulSoup(html, 'html.parser')

        driver.close()


scraper = FootballScraper()
scraper.scrape()