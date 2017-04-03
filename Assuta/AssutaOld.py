from Assuta.Assuta import Assuta
from Models.Person.Doctor import Doctor


class AssutaOld(Assuta):
    def __init__(self):
        Assuta.__init__(self)

    def save_doctors(self):
        self.driver.get('http://assuta-hospital.com/nashi-vrachi.aspx')
        links2 = [link.get_attribute('href') for link in
                  self.driver.find_elements_by_xpath("//ul[@class='doctorSlider_list js-doctorSlider_list']/li/a")]
        ent_list = []
        ophthalmologist_list = []
        surgeon_list = []
        uro_gynecology_list = []
        ent_flag = True
        ophthalmologist_flag = True
        surgeon_flag = True
        uro_gynecology_flag = True
        for link in links2:
            # print('{}'.format(link))
            self.driver.get(link)
            name = self.driver.find_element_by_xpath('//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/'
                                                     'table/tbody/tr/td[2]/div[2]/div/div/h1')
            # print('* ', name.text)

            if name.text == 'ЛОР-СПЕЦИАЛИСТЫ' and ent_flag is True:
                ent_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/p')]
                ent_flag = False

            if name.text == 'НАШИ ОФТАЛЬМОЛОГИ' and ophthalmologist_flag is True:
                ophthalmologist_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/div[2]/p')]
                ophthalmologist_flag = False

            if name.text == 'ПЛАСТИЧЕСКИЕ ХИРУРГИ' and surgeon_flag is True:
                surgeon_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/div[2]')]
                surgeon_flag = False

            if name.text == 'УРОГИНЕКОЛОГИ' and uro_gynecology_flag is True:
                uro_gynecology_list = [link.text for link in self.driver.find_elements_by_xpath(
                    '//*[@id="dBody"]/center/table/tbody/tr[3]/td/div/table/tbody/tr/td[2]/div[2]/div/div[1]/p')]
                uro_gynecology_flag = False
            # doctor = Doctor(name=name.text, birthday='', vacation='', image='', language='', info='', department='',
            #                 subDepartment='', visible_tg='', status='', first_tg='', link='')
            # doctor.save()
        # AssutaOld.save_doctors_from_sublist(ent_list[1::])
        # AssutaOld.save_doctors_from_sublist(ophthalmologist_list)
        # AssutaOld.save_doctors_from_sublist([el for el in surgeon_list if el.text == 'Подробнее >>'])
        tmp = [surgeon_list.index(el) for el in surgeon_list if el == 'Подробнее >>']

        tmp2 = [el for el in surgeon_list[::-1] if surgeon_list.index(el) == tmp[::-1]]
        for el in tmp2:
            print(el)
        # for el in surgeon_list:
        #     print(el)
        # AssutaOld.save_doctors_from_sublist(uro_gynecology_list[1::])

    @staticmethod
    def save_doctors_from_sublist(doctors_list):
        for doctor in doctors_list[::2]:
            index = doctors_list.index(doctor)
            doctor = Doctor(name=doctor, birthday='', vacation='', image='', language='', info=doctors_list[index + 1],
                            department='', subDepartment='', visible_tg='', status='', first_tg='', link='')
            doctor.save()

            # def print_doctors_info(self):
            #     for el in self.get_doctors_links():
            #         print(el.get_attribute('href'))
            #     self.driver.quit()
