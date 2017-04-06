from Assuta.Assuta import Assuta
from Models.Person.Doctor import Doctor
from selenium.webdriver.common.keys import Keys
import time


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
        username.send_keys("")
        password.send_keys("")
        form = self.driver.find_element_by_id('LoginForm')
        form.submit()

    def fill_doctors_info(self):
        print('start doctors')
        self.go_to_doctors()
        # result = self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div/h1')
        self.delete_all_doctors_info()
        counter = 0
        for doctor in Doctor.select():
            self.add_new_doctor(doctor)
            # if counter < 3:
            #     counter += 1
            # else:
            #     break

    def delete_all_doctors_info(self):
        print('start delete all doctors info')
        select_all = self.driver.find_element_by_xpath('//*[@id="select-all"]')
        self.mouse.move_to_element(select_all).click().perform()
        # time.sleep(1)
        delete_all = self.driver.find_element_by_xpath('//*[@id="button-delete"]')
        self.mouse.move_to_element(delete_all).click().perform()
        print('Has finished delete all doctors info')

    def add_new_doctor(self, doctor):
        print('Start add doctor')
        self.go_to_add_new_doctor()
        visible_tg = self.driver.find_element_by_xpath('//*[@id="MyPageForm"]/div[1]/div[1]/div/div/div/label')
        name = self.driver.find_element_by_xpath('//*[@id="Name"]')
        name.send_keys(f'{doctor.academic_title} {doctor.first_name} {doctor.second_name}')
        status = self.driver.find_element_by_xpath('//*[@id="ddStatus"]/option[3]').click()
        upload_image = self.driver.find_element_by_xpath('//*[@id="Image"]')
        first_tg = self.driver.find_element_by_xpath('//*[@id="MyPageForm"]/div[2]/div[1]/div/div/div/span[2]')
        language = self.driver.find_element_by_xpath('//*[@id="ddCulture"]')
        department = self.driver.find_element_by_xpath('//*[@id="ddDepartment"]/option[3]').click()
        # subdepartment = self.driver.find_element_by_xpath('//*[@id="ddSubdepartment"]/option[2]').click()
        doctor_info = self.driver.find_element_by_xpath('//*[@id="DocInfo"]')
        doctor_info.send_keys(doctor.info)
        # link = self.driver.find_element_by_xpath('//*[@id="ddLink"]/option[2]').click()
        # link = self.driver.find_element_by_xpath('//*[@id="s2id_autogen5"]')
        # create_btn = self.driver.find_element_by_xpath('//*[@id="btnInsert"]')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="s2id_ddLink"]/a/span[1]').click()
        link = self.driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
        link.send_keys(doctor.link)
        time.sleep(1)
        link.send_keys(Keys.ENTER)
        # upload_image.send_keys(image_url)
        # doctor_info.send_keys(doctor_info_desc)
        # link.send_keys(link_link)
        # time.sleep(5)
        print('form start')
        add_new_doctor_form = self.driver.find_element_by_id('MyPageForm')
        add_new_doctor_form.submit()
        print('form end')
        # time.sleep(3)
        # back = self.driver.find_element_by_xpath('//*[@id="MyPageForm"]/div[5]/div/div/a')
        # self.mouse.move_to_element(back).click().perform()

    def go_to_add_new_doctor(self):
        time.sleep(3)
        self.driver.get('http://new.assuta-hospital.com/Admin/Doctor/New')

    def go_to_doctors(self):
        time.sleep(3)
        self.driver.get('http://new.assuta-hospital.com/Admin/Doctor')

    def session_end(self):
        self.driver.quit()
