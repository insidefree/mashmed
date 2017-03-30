import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time

URL_DOCTORS_OLD_SITE = 'http://assuta-hospital.com/nashi-vrachi.aspx'
URL_EXAMPLE = 'https://www.google.co.il/?gfe_rd=cr&ei=iQrdWIbIHaag8we_hL6QCA&gws_rd=ssl'

class Doctors(object):
    def __init__(self):
        self.driver = webdriver.Chrome()


def sel():
    driver = webdriver.PhantomJS()
    driver.get(URL_DOCTORS_OLD_SITE)
    time.sleep(3)
    print(driver.find_element_by_class_name("doctorSlider_list js-doctorSlider_list").text)
    driver.close()


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('div', class_='cut_doctorSlider_list')
    print(soup.prettify())


def main():
    # doctors = Doctors()
    # print(doctors.driver.get(URL_DOCTORS_OLD_SITE))
    # test = doctors.driver.find_element_by_class_name('doctorSlider_list')
    # print('test', test)
    # soup = BeautifulSoup(test, 'html.parser')
    # print('soup', soup.find_element_by_class_name('doctorSlider_list'))
    # doctors.driver.quit()
    # print(parse(get_html(URL_DOCTORS_OLD_SITE)))

    driver = webdriver.Chrome()
    html = driver.get('http://assuta-hospital.com/nashi-vrachi.aspx')
    # print(driver.page_source.encode('utf-8'))
    elements = []
    elements =  driver.find_elements_by_xpath("//ul[@class='doctorSlider_list js-doctorSlider_list']/li/a")
    # elements =  driver.find_elements_by_xpath("//li")
    # print(elements)
    for e in elements:
        print(e.get_attribute('href'))
    driver.quit()
    

if __name__ == '__main__':
    main()
