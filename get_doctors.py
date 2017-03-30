import urllib.request
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import time

URL_DOCTORS_OLD_SITE = 'http://assuta-hospital.com/nashi-vrachi.aspx'


def sel():
    driver = webdriver.PhantomJS(executable_path=r'C:\Users\denys-s\Documents\Projects\mashmed\utils\phantomjs')
    driver.get(URL_DOCTORS_OLD_SITE)
    time.sleep(3)
    print(driver.find_element_by_class_name("doctorSlider_list js-doctorSlider_list").text)
    driver.close()


class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


r = Render(URL_DOCTORS_OLD_SITE)
html = r.frame.toHtml()


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('div', class_='cut_doctorSlider_list')
    print(soup.prettify())


def main():
    # parse(get_html(URL_DOCTORS_OLD_SITE))
    sel()


if __name__ == '__main__':
    main()
