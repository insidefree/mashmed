from Assuta.Assuta import Assuta
from Models.Person.Doctor import Doctor
import selenium.webdriver.support.ui as ui
import time


class AssutaOld(Assuta):
    def __init__(self):
        Assuta.__init__(self)

    def save_doctors(self):
        links = self.get_doctors_links()
        wait = ui.WebDriverWait(self.driver, 5000)
        for link in links:
            self.driver.get(link.get_attribute('href'))
            time.sleep(10)
            name = self.driver.find_element_by_xpath('//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/'
                                                     'table/tbody/tr/td[2]/div[2]/div/div/h1')
            doctor = Doctor(name=name.text, birthday='', vacation='', image='', language='', info='', department='',
                            subDepartment='', visible_tg='', status='', first_tg='', link='')
            doctor.save()
            time.sleep(10)
            self.driver.quit()
            time.sleep(30)

    def get_doctors_links(self):
        self.driver.get('http://assuta-hospital.com/nashi-vrachi.aspx')
        return self.driver.find_elements_by_xpath("//ul[@class='doctorSlider_list js-doctorSlider_list']/li/a")

    def print_doctors_info(self):
        for el in self.get_doctors_links():
            print(el.get_attribute('href'))
        self.driver.quit()
