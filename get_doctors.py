from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class Assuta():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.mouse = webdriver.ActionChains(self.driver)


class AssutaOld(Assuta):
    def __init__(self):
        Assuta.__init__(self)

    def get_doctors_info(self):
        self.driver.get('http://assuta-hospital.com/nashi-vrachi.aspx')
        return self.driver.find_elements_by_xpath("//ul[@class='doctorSlider_list js-doctorSlider_list']/li/a")

    def print_doctors_info(self):
        for el in self.get_doctors_info():
            print(el.get_attribute('href'))
        self.driver.quit()


class AssutaNew(Assuta):
    def __init__(self):
        Assuta.__init__(self)
        self.username = ''
        self.password = ''

    def sing_in(self):
        print('start login')
        self.driver.get('http://new.assuta-hospital.com/Admin')
        username = self.driver.find_element_by_id("UserName")
        password = self.driver.find_element_by_id("Password")
        username.send_keys("denys.sorokin")
        password.send_keys("8mfBQn")
        form = self.driver.find_element_by_id('LoginForm')
        form.submit()

    def fill_doctors_info(self):
        print('start doctors')
        self.go_to_doctors()
        result = self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div/h1')
        self.delete_all_doctors_info()
        self.add_new_doctor()
        return result

    def delete_all_doctors_info(self):
        print('start delete all doctors info')
        select_all = self.driver.find_element_by_xpath('//*[@id="select-all"]')
        self.mouse.move_to_element(select_all).click().perform()
        time.sleep(1)
        delete_all = self.driver.find_element_by_xpath('//*[@id="button-delete"]')
        self.mouse.move_to_element(delete_all).click().perform()
        print('Has finished delete all doctors info')

    def add_new_doctor(self):
        print('Start add doctor')
        self.go_to_add_new_doctor()
        visible_tg = self.driver.find_element_by_xpath('//*[@id="MyPageForm"]/div[1]/div[1]/div/div/div/label')
        name = self.driver.find_element_by_xpath('//*[@id="Name"]')
        status = self.driver.find_element_by_xpath('//*[@id="ddStatus"]/option[1]').click()
        upload_image = self.driver.find_element_by_xpath('//*[@id="Image"]')
        first_tg = self.driver.find_element_by_xpath('//*[@id="MyPageForm"]/div[2]/div[1]/div/div/div/span[2]')
        language = self.driver.find_element_by_xpath('//*[@id="ddCulture"]')
        department = self.driver.find_element_by_xpath('//*[@id="ddDepartment"]/option[3]').click()
        subdepartment = self.driver.find_element_by_xpath('//*[@id="ddSubdepartment"]/option[4]').click()
        doctor_info = self.driver.find_element_by_xpath('//*[@id="DocInfo"]')
        link = self.driver.find_element_by_xpath('//*[@id="s2id_ddLink"]/a/span[1]')
        # create_btn = self.driver.find_element_by_xpath('//*[@id="btnInsert"]')

        name.send_keys('qwe')
        upload_image.send_keys('http://new.assuta-hospital.com/Content/ru-RU/images/doctors/alexander_belenkyi.jpg')
        doctor_info.send_keys('qwe')
        link.send_keys('/TEST/TEST/TEST')

        add_new_doctor_form = self.driver.find_element_by_id('MyPageForm')
        add_new_doctor_form.submit()

    def go_to_add_new_doctor(self):
        time.sleep(5)
        self.driver.get('http://new.assuta-hospital.com/Admin/Doctor/New')

    def go_to_doctors(self):
        time.sleep(3)
        self.driver.get('http://new.assuta-hospital.com/Admin/Doctor')

    def session_end(self):
        self.driver.quit()


def main():
    # assuta = AssutaOld()
    # assuta.print_doctors_info()
    assuta_new = AssutaNew()
    assuta_new.sing_in()
    print(assuta_new.fill_doctors_info().text)

    assuta_new.session_end()

if __name__ == '__main__':
    main()
