from selenium import webdriver


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
        self.session_start_doctors()
        return self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div/h1')

    def delete_all_doctors_info(self):
        print('start delete all doctors info')
        self.session_start_doctors()
        select_all = self.driver.find_element_by_xpath('//*[@id="select-all"]')
        self.mouse.move_to_element(select_all).click().perform()
        delete_all = self.driver.find_element_by_xpath('//*[@id="button-delete"]')
        self.mouse.move_to_element(delete_all).click().perform()

    def session_start_doctors(self):
        self.driver.get('http://new.assuta-hospital.com/Admin/Doctor')

    def session_end(self):
        self.driver.quit()


def main():
    # assuta = AssutaOld()
    # assuta.print_doctors_info()
    assuta_new = AssutaNew()
    assuta_new.sing_in()
    print(assuta_new.fill_doctors_info().text)

    assuta_new.delete_all_doctors_info()
    assuta_new.session_end()

if __name__ == '__main__':
    main()
