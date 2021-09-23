# coding=utf8
import json
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def findAttributeFromView(element, att):
    try:
        return element[att]
    except:
        return ''


def createWebDriver():
    return webdriver.Chrome('./service/chromedriver.exe', options=setWebDriverOptions())


def setWebDriverOptions():
    options = webdriver.ChromeOptions()
    options.headless = True
    return options


def search(driver, url):
    driver.get(url)

    if(driver.current_url == url):
        return True
    else:
        return False


def acceptCookies(driver):
    buttons = driver.find_element_by_css_selector(
        '#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.qqtRac > form > div.lssxud > div > button')
    buttons.click()


def webPageHasLoaded(driver):
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "grid-container")))

    if(element != None):
        return True
    else:
        return False


def save(data):
    my_file = open('youtube_trends_data.json', 'w')
    scraped = json.dumps(data, indent=4)
    my_file.write(scraped)
    my_file.close()


def getAllViews(webDriver):
    return BeautifulSoup(
        webDriver.page_source, 'html.parser').find_all('ytd-video-renderer')


def getThumbnail(url):
    id = url.split("=")[1]
    return 'https://img.youtube.com/vi/' + id + '/hqdefault.jpg'


def parseDataFromAllViews(webDriver):

    if(webPageHasLoaded(webDriver)):

        views = list()

        for view in getAllViews(webDriver):

            url = 'https://www.youtube.com' + \
                findAttributeFromView(view.a, 'href')
            title = view.h3.text
            thumbnail = getThumbnail(url)
            channelName = view.find(
                "a", {"class": "yt-simple-endpoint style-scope yt-formatted-string"}).text
            viewAge = view.find_all(
                'span', {"class": "style-scope ytd-video-meta-block"})

            data = {
                'url': url,
                'thumbnail': thumbnail,
                'title': title,
                'channel_name': channelName,
                'views': viewAge[0].text,
                'age': viewAge[1].text
            }

            views.append(data)
        return views


def showSuccessMessage():
    print("\033c")
    print('Successfull')


def main():
    webDriver = createWebDriver()
    search(webDriver, 'https://www.youtube.com/feed/trending')
    acceptCookies(webDriver)
    data = parseDataFromAllViews(webDriver)
    # save(data)
    json.dump({"data": data}, sys.stdout)
    sys.stdout.flush()
    # showSuccessMessage()
    webDriver.quit()


if __name__ == '__main__':
    main()
